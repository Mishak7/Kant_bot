from aiogram import Bot, Dispatcher
from config.settings import settings
from config.logger import logger
from handlers import commands, messages
from handlers.dormitory_handlers import dormitory_handlers, dormitory_location_handlers
from handlers.critical_info_handlers import critical_handler
from handlers.location_handlers import location_handlers
from handlers.hospital_handlers import hospital_handler
from handlers.university_handlers import university_info_handlers


async def main():
    bot = Bot(token=settings.TELEGRAM_TOKEN)
    dp = Dispatcher()

    dp.include_router(commands.router)
    dp.include_router(messages.router)
    dp.include_router(dormitory_handlers.router)
    dp.include_router(critical_handler.router)
    dp.include_router(location_handlers.router)
    dp.include_router(hospital_handler.router)
    dp.include_router(university_info_handlers.router)
    dp.include_router(dormitory_location_handlers.router)

    try:
        logger.info('Bot started')
        await dp.start_polling(bot)
    except Exception as e:
        logger.critical(f'Bot crashed: {e}')
    finally:
        await bot.session.close()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
