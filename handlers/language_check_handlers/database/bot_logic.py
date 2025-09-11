# авторизация

import sqlite3
import aiosqlite
from config.logger import logger
from langchain_gigachat.chat_models import GigaChat
from langchain_core.messages import SystemMessage
from handlers.language_check_handlers.database.prompts.evaluation_prompt import evaluation_prompt
from handlers.language_check_handlers.database.speech_utils import transcribe_voice_message

db = sqlite3.connect('BFU')
cursor = db.cursor()

gigachat = GigaChat(temperature = 0,
                    top_p = 0.1,
                    credentials=...,
                    verify_ssl_certificate=False)

# при авторизации получаем telegram_id и username пользователя
# выводит id юзера 
async def get_user_id(inserted_telegram_id):
    try:
        async with aiosqlite.connect('BFU.db') as db:
            cursor = await db.execute("SELECT id FROM Users WHERE telegram_id = ?", (inserted_telegram_id,))
            user = await cursor.fetchone()
            if user:
                return user[0]
            else:
                return "User not found"
    except Exception as e:
        logger.error(f"Error in get_user_id: {e}")
        return None

# надо прописать логику, чтобы name_level это было название той кнопки, которую нажимает пользователь
async def get_task(name_level, user_id): # user_id - результат работы функции get_user_id
    '''
    name_level - кнопка, которую нажал пользователь (надо как-то прописать эту логику)
    user_id - результат работы функции get_user_id
    '''
    try:
        async with aiosqlite.connect('BFU.db') as db:
            cursor = await db.execute("SELECT score FROM UserModules WHERE user_id = ? AND level_name=?", (user_id, name_level))
            row = await cursor.fetchone()
            user_score = row[0] if row else 0

            if user_score < 30:
                module_type = 'Easy'
            elif 30 <= user_score < 60:
                module_type = 'Middle'
            else:
                module_type = 'Senior'

            cursor = await db.execute("SELECT level_id FROM Levels WHERE level_name = ?", (name_level,))
            row = await cursor.fetchone()
            level_id = row[0] if row else None

            cursor = await db.execute("SELECT module_id FROM Modules WHERE module_name = ?", (module_type,))
            module = await cursor.fetchone()
            module_id = module[0] if module else None

            cursor = await db.execute("SELECT task_id, content, question FROM Tasks WHERE module_id =? AND level_id = ? ORDER BY RANDOM() LIMIT 1", (module_id, level_id))
            row = await cursor.fetchone()
            return row
    
    except Exception as e:
        logger.error(f"Error getting a task: {e}")
        return False


async def prepare_question(task):
    '''
    Функция prepare_question формирует в удобном ответе результат выбора рандомного задания из бд.

    task - результат работы функции get_task.
    '''
    task_id, content, question, audio = task
    if audio:
        return {"task_id": task_id, "content": content, "question": question, "audio": audio}
        # в выводе задания пользователю мы выводим только question, audio
        # content, task_id нам нужны доя проверки
    else:
        return {"task_id": task_id, "content": content, "question": question}
    

async def extract_audio_from_db(task_id: str):
    '''
    Функция для извлечения аудио из бд.
    '''
    async with aiosqlite.connect('BFU.db') as db:
        cursor = await db.execute("SELECT audio FROM Tasks WHERE task_id=?", (task_id,))
        row = await cursor.fetchone()

        if row and row[0]:
            audio_blob = row[0]
            with open('audio.blob', f'extracted_audio{task_id}.wav') as f:
                f.write(audio_blob)


# тут дальше в коде мы получаем идентификтор из функции get_task
async def check_task(user_ident, task_ident, user_answer, is_voice=False):
    '''
    user_ident - идентификатор пользователя из get_user_id
    task_ident - идентификатор задания из get_task
    user_answer - ответ пользователя на задание, которое было выбрано в get_task
    is_voice - True если ответ юзера это голосовое (задание на спикинг)
    '''
    try:
        async with aiosqlite.connect('BFU.db') as db:
            cursor = await db.execute("SELECT correct_answer FROM TasksAnswers WHERE task_id=?", (task_ident,))
            row = await cursor.fetchone()[0]
            check_answ = row[0] if row else None

            cursor = await db.execute("""
                    SELECT T.type, T.score, T.level_id, T.question, T.content, L.level_name
                    FROM Tasks T
                    JOIN Levels L ON T.level_id = L.level_id
                    WHERE T.task_id=?
                """, (task_ident,))
            task_row = cursor.fetchone()
            type_task, score_change, level_id, question, content, level_name = task_row

            if check_answ:
                if user_answer == check_answ:
                    await db.execute("""UPDATE UserModules 
                        SET score = score + ? 
                        WHERE user_id = ? AND level_id = ?
                        """, (score_change, user_ident, level_id))
                    await db.commit()
                    return 'верно'
                else:
                    await db.execute("""UPDATE UserModules
                        SET score = score - ?
                        WHERE user_id = ? AND level_id = ?
                        """, (score_change, user_ident, level_id))
                    await db.commit()
                    return 'неверно'
                    
            if is_voice:
                user_answer = transcribe_voice_message(user_answer) # ТУТ НАДО ПОМЕНЯТЬ ПАРАМЕТР! Когда будет настроена логика ответ человека в гс должен сохраняться у нас где-то как путь

                prompt = evaluation_prompt.format(
                    content=content,
                    question=question,
                    user_answer=user_answer,
                    level_name=level_id,
                    type_question=type_task
                )
                response = gigachat.invoke([
                    SystemMessage(content=prompt)
                ])
                # здесь надо прописать, как очки добавлять, если открытый ответ (в промпте должно быть)
                return response.content
    except Exception as e:
        logger.error(f"Error checking user answer: {e}")
        return False
    

async def check_user_exists(telegram_id: int) -> bool:
    try:
        async with aiosqlite.connect('BFU.db') as db:
            cursor = await db.execute("SELECT id FROM Users WHERE telegram_id = ?", (telegram_id,))
            result = await cursor.fetchone()
            return result is not None
    except Exception as e:
        logger.error(f"Error checking user existence: {e}")
        return False


async def create_user(telegram_id: int, username: str):
    try:
        async with aiosqlite.connect('BFU.db') as db:
            user = check_user_exists(telegram_id)
            if not user:
                await db.execute("""
                    INSERT INTO Users (telegram_id, username, score, hearts, created_at, updated_at)
                    VALUES (?, ?, 0, 5, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                """, (telegram_id, username))
                await db.commit()
                return True
            else:
                return 'This user already exists'
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        return False

async def get_user_name(telegram_id: int) -> str:
    try:
        user = check_user_exists(telegram_id)
        if user:
            async with aiosqlite.connect('BFU.db') as db:
                cursor = await db.execute(
                    "SELECT username, score, hearts FROM Users WHERE telegram_id = ?",
                    (telegram_id,)
                )
                result = await cursor.fetchone()
                return result if result else None
        else:
            return 'User does not exist'
    except Exception as e:
        logger.error(f"Error getting user name: {e}")
        return None