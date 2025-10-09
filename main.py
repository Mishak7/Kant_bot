from aiogram import Bot, Dispatcher
from config.settings import settings
from config.logger import logger
from handlers.main_handlers import commands
from handlers.dormitory_handlers import dormitory_handlers, dormitory_location_handlers
from handlers.critical_info_handlers import critical_handler
from handlers.location_handlers import location_handlers
from handlers.hospital_handlers import hospital_handler
from handlers.university_handlers import university_info_handlers
from handlers.language_check_handlers.grammar_handlers import grammar_handlers
from handlers.language_check_handlers.listening_handlers import listening_handlers
from handlers.language_check_handlers.speaking_handlers import speaking_handlers
from handlers.sber_handlers import sber_handlers
from aiogram.fsm.storage.memory import MemoryStorage
from handlers.level_selection_handlers import level_selection_handler
from services.database.database_fill import data
from services.database.database_functions import add_tasks
from handlers.places_to_visit_handlers import places_to_visit_handler

from aiogram import BaseMiddleware
from typing import Callable, Dict, Any, Awaitable
from aiogram.types import TelegramObject
import aiosqlite
import asyncio
import os


class LanguageMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        state = data['state']
        user_data = await state.get_data()
        data['language'] = user_data.get('language', 'ru')
        return await handler(event, data)


async def init_db():
    """Асинхронная инициализация базы данных"""
    if os.path.exists('BFU.db'):
        logger.info("Database already exists")
        return

    async with aiosqlite.connect('BFU.db') as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS Levels (
        level_id INTEGER PRIMARY KEY AUTOINCREMENT,
        level_score INTEGER,
        level_name TEXT
        )
        """
                         )

        await db.execute("""
        CREATE TABLE IF NOT EXISTS Modules (
        module_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        module_name TEXT
        )
        """
                         )

        await db.execute("""
        CREATE TABLE IF NOT EXISTS LevelsModules(
        level_id INTEGER, 
        module_id INTEGER, 
        FOREIGN KEY(level_id) REFERENCES Levels(level_id),
        FOREIGN KEY(module_id) REFERENCES Modules(module_id), 
        PRIMARY KEY (level_id, module_id)
        )
        """
                         )

        await db.execute("""
        CREATE TABLE IF NOT EXISTS Tasks(
        task_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        level_id INTEGER, 
        module_id INTEGER,
        type TEXT NOT NULL,
        content TEXT NOT NULL, 
        question TEXT NOT NULL, 
        audio BLOB DEFAULT NULL,
        score INTEGER DEFAULT 10,
        check_method TEXT,
        FOREIGN KEY(level_id) REFERENCES Levels(level_id),
        FOREIGN KEY(module_id) REFERENCES Modules(module_id)
        )
        """
                         )

        await db.execute("""
        CREATE TABLE IF NOT EXISTS TasksAnswers(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        task_id INTEGER, 
        correct_answer, 
        FOREIGN KEY(task_id) REFERENCES Tasks(task_id)
        )
        """
                         )

        await db.execute("""
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        telegram_id BIGINT UNIQUE NOT NULL, 
        username TEXT, 
        score INTEGER, 
        hearts INTEGER, 
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
                         )

        # изменила module_id на level_id (чтобы мы сохраняли именно прогресс по уровню, а не easy и тд модулям
        await db.execute("""
        CREATE TABLE IF NOT EXISTS UserModules(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        user_id INTEGER, 
        level_id INTEGER,
        level_name TEXT,
        score INTEGER DEFAULT 0, 
        is_completed BOOLEAN DEFAULT FALSE, 
        completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
        FOREIGN KEY(user_id) REFERENCES Users(id), 
        FOREIGN KEY(level_id) REFERENCES Levels(level_id),
        FOREIGN KEY(level_name) REFERENCES Levels(level_name)
        )
        """
                         )

        await db.execute("""
        CREATE TABLE IF NOT EXISTS UserProgress(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        user_id INTEGER, 
        task_id INTEGER, 
        user_answer TEXT, 
        is_correct BOOLEAN NOT NULL, 
        score_earned INTEGER, 
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
        FOREIGN KEY(user_id) REFERENCES Users(id), 
        FOREIGN KEY(task_id) REFERENCES Tasks(task_id)
        )
        """
                         )

        await db.commit()

        cursor = await db.execute("PRAGMA table_info(Tasks)")
        columns = [row[1] for row in await cursor.fetchall()]

        if "check_method" not in columns:
            await db.execute("ALTER TABLE Tasks ADD COLUMN check_method TEXT")
            await db.commit()
            logger.info("Добавлен столбец check_method в таблицу Tasks")

        cursor = await db.execute("PRAGMA table_info(Tasks)")
        columns = [row[1] for row in await cursor.fetchall()]

        if "check_method" not in columns:
            await db.execute("ALTER TABLE Tasks ADD COLUMN check_method TEXT")
            await db.commit()
            logger.info("Добавлен столбец check_method в таблицу Tasks")

        logger.info("База данных инициализирована")


async def main():
    await init_db()
    await add_tasks(data=data)

    bot = Bot(token=settings.TELEGRAM_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.update.middleware(LanguageMiddleware())

    dp.include_router(commands.router)
    dp.include_router(dormitory_handlers.router)
    dp.include_router(critical_handler.router)
    dp.include_router(location_handlers.router)
    dp.include_router(hospital_handler.router)
    dp.include_router(university_info_handlers.router)
    dp.include_router(dormitory_location_handlers.router)
    dp.include_router(grammar_handlers.router)
    dp.include_router(listening_handlers.router)
    dp.include_router(speaking_handlers.router)
    dp.include_router(sber_handlers.router)
    dp.include_router(level_selection_handler.router)
    dp.include_router(places_to_visit_handler.router)

    from aiohttp import web
    from aiogram.types import Update
    app = web.Application()

    async def webhook_handler(request):
        update_data = await request.json()
        update = Update(**update_data)
        await dp.feed_update(bot, update)
        return web.Response(status=200)

    app.router.add_post('/webhook', webhook_handler)

    if os.getenv('TEST_MODE'):
        logger.info('Starting in WEBHOOK mode for testing')
        web.run_app(app, host='0.0.0.0', port=8080)
    else:
        logger.info('Starting in POLLING mode')
        await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
