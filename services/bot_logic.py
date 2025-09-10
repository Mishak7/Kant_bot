# авторизация

import sqlite3
import aiosqlite
from config.logger import logger

db = sqlite3.connect('BFU')
cursor = db.cursor()

# при авторизации получаем telegram_id и username пользователя
# выводит id юзера 
async def get_user_id(inserted_telegram_id, inserted_username):
    try:
        async with aiosqlite.connect('BFU.db') as db:
            async with db.cursor() as cursor:
                await cursor.execute("SELECT id FROM Users WHERE telegram_id = ?", (inserted_telegram_id,))
                user = await cursor.fetchone()
                if user:
                    return user[0]
                else:
                    success = await create_user(inserted_telegram_id, inserted_username)
                    if success:
                        await cursor.execute("SELECT id FROM Users WHERE telegram_id = ?", (inserted_telegram_id,))
                        user = await cursor.fetchone()
                        await db.commit()
                        return user[0] if user else None
                    else:
                        logger.error("Failed to create user")
                        await db.rollback()
                        return None
    except Exception as e:
        logger.error(f"Error in get_user_id: {e}")
        return None

# надо прописать логику, чтобы name_level это было название той кнопки, которую нажимает пользователь
def get_task(name_level, user_id): # user_id - результат работы функции get_user_id
    cursor.execute("SELECT score FROM UserModules WHERE user_id = ? AND level_name=?", (user_id, name_level))
    user_score = cursor.fetchone()[0]
    if user_score < 30:
        module_type = 'Easy'
    elif 30 <= user_score < 60:
        module_type = 'Middle'
    else:
        module_type = 'Senior'

    cursor.execute("SELECT module_id FROM Modules WHERE module_name = ?", (module_type,))
    module = cursor.fetchone()
    if not module:
        return None
    module_id = module[0]

    cursor.execute("SELECT task_id, content, question FROM Tasks WHERE module_id = ? ORDER BY RANDOM() LIMIT 1", (module_id,))
    return cursor.fetchone()

# тут дальше в коде мы получаем идентификтор из функции get_task
def check_task_grammar_reading(user_ident, task_ident, user_answer):
    cursor.execute("SELECT correct_answer FROM TasksAnswers WHERE task_id=?", (task_ident,))
    check_answ = cursor.fetchone()[0]
    if check_answ:
        cursor.execute("SELECT score FROM Tasks WHERE task_id=?", (task_ident,))
        score_change = cursor.fetchone()[0]
        if user_answer == check_answ:
            cursor.execute("""UPDATE UserModules 
                SET score = score + ? 
                WHERE user_id = (SELECT id FROM Users WHERE id = ?) 
                AND level_id = (SELECT level_id FROM Tasks WHERE task_id = ?)
                """, (score_change, user_ident, task_ident))
            return 'correct'
        else:
            cursor.execute("""UPDATE UserModules
                SET score = score - ?
                WHERE user_id = (SELECT id FROM Users WHERE id = ?) 
                AND level_id = (SELECT level_id FROM Tasks WHERE task_id = ?)
                """, (score_change, user_ident, task_ident))
            return 'not correct' # тут нужно будет использовать эту функцию в самой логике работы, чтобы потом
            # ориентируясь на аутпут функции либо выводить объяснение правильного ответа с помощью гигачата + текущи скор
            # либо просто выводить а-ля "Вы молодец" и текущий скор


async def create_user(telegram_id: int, username: str):
    try:
        async with aiosqlite.connect('BFU.db') as db:
            await db.execute("""
                INSERT INTO Users (telegram_id, username, score, hearts, created_at, updated_at)
                VALUES (?, ?, 0, 5, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
            """, (telegram_id, username))
            await db.commit()
            return True
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        return False

async def get_user_name(telegram_id: int) -> str:
    try:
        async with aiosqlite.connect('BFU.db') as db:
            cursor = await db.execute(
                "SELECT username, score, hearts FROM Users WHERE telegram_id = ?",
                (telegram_id,)
            )
            result = await cursor.fetchone()
            return result if result else None
    except Exception as e:
        logger.error(f"Error getting user name: {e}")
        return None