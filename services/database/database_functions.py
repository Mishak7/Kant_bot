import aiosqlite
import os
import tempfile
from config.logger import logger
from typing import Optional
from langchain_gigachat.chat_models import GigaChat
from langchain_core.messages import SystemMessage
from services.database.database_prompts.evaluation_prompt import evaluation_prompt
from services.database.speech_utils import transcribe_voice_message, text_to_speech
from config.settings import Settings
import json
from aiogram.types import FSInputFile


#ОЧЕНЬ ВРЕМЕННО - спрятать такое лучше
gigachat = GigaChat(temperature=0,
                    top_p=0.1,
                    credentials=Settings.GIGA_CREDENTIALS,
                    model="GigaChat-2-Max",
                    verify_ssl_certs=False)


async def add_tasks(
    data=None,
    level_score=None,
    level_name=None,
    module_name=None,
    type_task=None,
    task_content=None,
    task_question=None,
    check_method=None,
    task_score=None,
    answer=None,
    with_audio=False
):
    async def add_single_task(
        db,
        level_score,
        level_name,
        module_name,
        type_task,
        task_content,
        task_question,
        check_method,
        task_score,
        answer=None,
        with_audio=False
    ):
        async with db.cursor() as cursor:
            await cursor.execute("SELECT level_id FROM Levels WHERE level_name=?", (level_name,))
            row = await cursor.fetchone()
            if row:
                level_id = row[0]
            else:
                await cursor.execute("INSERT INTO Levels (level_score, level_name) VALUES(?, ?)",
                                    (level_score, level_name))
                level_id = cursor.lastrowid

            await cursor.execute("SELECT module_id FROM Modules WHERE module_name=?", (module_name,))
            row = await cursor.fetchone()
            if row:
                module_id = row[0]
            else:
                await cursor.execute("INSERT INTO Modules (module_name) VALUES(?)", (module_name,))
                module_id = cursor.lastrowid

            await cursor.execute("SELECT 1 FROM LevelsModules WHERE level_id=? AND module_id=?", (level_id, module_id))
            if not await cursor.fetchone():
                await cursor.execute("INSERT INTO LevelsModules(level_id, module_id) VALUES(?, ?)", (level_id, module_id))

            await cursor.execute("SELECT task_id FROM Tasks WHERE question=? AND content=?", (task_question, task_content))
            row = await cursor.fetchone()
            if not row:
                if with_audio:
                    audio_path = text_to_speech(task_content, "temp.wav")
                    with open(audio_path, "rb") as f:
                        audio_blob = f.read()
                    await cursor.execute("""
                        INSERT INTO Tasks(level_id, module_id, type, content, question, score, check_method, audio)
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?)
                    """, (level_id, module_id, type_task, task_content, task_question, task_score, check_method, audio_blob))
                    if os.path.exists(audio_path):
                        os.remove(audio_path)
                else:
                    await cursor.execute("""
                        INSERT INTO Tasks(level_id, module_id, type, content, question, score, check_method)
                        VALUES(?, ?, ?, ?, ?, ?, ?)
                    """, (level_id, module_id, type_task, task_content, task_question, task_score, check_method))
                task_id = cursor.lastrowid
            else:
                task_id = row[0]

            if answer is not None:
                await cursor.execute("""
                    INSERT INTO TasksAnswers (task_id, correct_answer)
                    VALUES (?, ?)
                """, (task_id, answer))
            await db.commit()

    async with aiosqlite.connect('BFU.db') as db:
        if data is not None:
            tasks = data.get("tasks", [])
            for task in tasks:
                await add_single_task(
                    db,
                    level_score=task.get("level_score"),
                    level_name=task.get("level_name"),
                    module_name=task.get("module_name"),
                    type_task=task.get("type_task"),
                    task_content=task.get("task_content"),
                    task_question=task.get("task_question"),
                    check_method=task.get("check_method"),
                    task_score=task.get("task_score"),
                    answer=task.get("answer"),
                    with_audio=task.get("with_audio", False)
                )
        else:
            await add_single_task(
                db,
                level_score=level_score,
                level_name=level_name,
                module_name=module_name,
                type_task=type_task,
                task_content=task_content,
                task_question=task_question,
                check_method=check_method,
                task_score=task_score,
                answer=answer,
                with_audio=with_audio
            )


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

async def check_user_exists(telegram_id: int) -> bool:
    try:
        async with aiosqlite.connect('BFU.db') as db:
            cursor = await db.execute("SELECT id FROM Users WHERE telegram_id = ?", (telegram_id,))
            result = await cursor.fetchone()
            return result is not None
    except Exception as e:
        logger.error(f"Error checking user existence: {e}")
        return False

async def get_user_name(telegram_id: int) -> Optional[str]:
    try:
        user = await check_user_exists(telegram_id)
        if user:
            async with aiosqlite.connect('BFU.db') as db:
                cursor = await db.execute(
                    "SELECT username, score, hearts FROM Users WHERE telegram_id = ?",
                    (telegram_id,)
                )
                result = await cursor.fetchone()
                return result if result else None
        else:
            return None
    except Exception as e:
        logger.error(f"Error getting user name: {e}")
        return None


async def get_module_progress(telegram_id: int, module_id: int) -> Optional[tuple]:
    """
    Асинхронно получает прогресс пользователя по заданному модулю.

    Выполняет запрос к базе данных для подсчёта суммы баллов, которые пользователь набрал в модуле,
    а также максимального количества баллов, которые можно получить в этом модуле,
    и вычисляет процент выполнения модуля.

    Args:
        telegram_id (int): Уникальный идентификатор пользователя в Telegram.
        module_id (int): Идентификатор модуля.

    Returns:
        Optional[tuple]: Кортеж из (user_id, module_id, user_score, max_score_in_module, процент_выполнения)
                         или None, если данные не найдены или возникла ошибка.
    """
    try:
        async with aiosqlite.connect('BFU.db') as db:
            cursor = await db.execute("""
                    SELECT UserProgress.user_id, Tasks.module_id, SUM(UserProgress.score_earned) AS user_score, (SELECT SUM(score) FROM Tasks WHERE module_id = ?) AS max_score_in_module, 100*SUM(UserProgress.score_earned)/(SELECT SUM(score) FROM Tasks WHERE module_id = ?)
                    FROM UserProgress JOIN Tasks ON UserProgress.task_id = Tasks.task_id
                    GROUP BY UserProgress.user_id, Tasks.module_id
                    HAVING UserProgress.user_id = ?""",
                                      (module_id, module_id, telegram_id,))

            result = await cursor.fetchone()
            return result if result else None

    except Exception as e:
        logger.error(f"Error getting module progress: {e}")
        return None


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
async def get_task(name_level, user_id):  # user_id - результат работы функции get_user_id
    """
    name_level - кнопка, которую нажал пользователь (надо как-то прописать эту логику)
    user_id - результат работы функции get_user_id
    """
    try:
        async with aiosqlite.connect('BFU.db') as db:
            cursor = await db.execute("SELECT score FROM UserModules WHERE user_id = ? AND level_name=?",
                                      (user_id, name_level))
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



            cursor = await db.execute(
                "SELECT task_id, content, question, audio FROM Tasks WHERE module_id =? AND level_id = ? ORDER BY RANDOM() LIMIT 1",
                (module_id, level_id))
            row = await cursor.fetchone()
            return row

    except Exception as e:
        logger.error(f"Error getting a task: {e}")
        return False


async def prepare_question(task):
    """
    Функция prepare_question формирует в удобном ответе результат выбора рандомного задания из бд.

    task - результат работы функции get_task.
    """
    task_id, content, question, audio = task
    # в выводе задания пользователю мы выводим только question, audio
    # content, task_id нам нужны доя проверки
    if audio:
        return {"task_id": task_id, "content": content, "question": question, "audio": audio}
    else:
        return {"task_id": task_id, "content": content, "question": question}


async def extract_audio_from_db(task_id: str) -> Optional[FSInputFile]:
    """
    Функция для извлечения аудио из БД и сохранения во временный файл.
    """
    async with aiosqlite.connect('BFU.db') as db:
        cursor = await db.execute("SELECT audio FROM Tasks WHERE task_id=?", (task_id,))
        row = await cursor.fetchone()

        if row and row[0]:
            audio_blob = row[0]

            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
                temp_file.write(audio_blob)
                file_path = temp_file.name

            input_file = FSInputFile(file_path)
            os.remove(file_path)

            return input_file
        else:
            return None


# тут дальше в коде мы получаем идентификтор из функции get_task
async def check_task(user_ident, task_ident, user_answer, is_voice=False):
    """
    user_ident - идентификатор пользователя из get_user_id
    task_ident - идентификатор задания из get_task
    user_answer - ответ пользователя на задание, которое было выбрано в get_task
    is_voice - True если ответ юзера это голосовое (задание на спикинг)
    """
    try:
        async with aiosqlite.connect('BFU.db') as db:
            cursor = await db.execute("SELECT correct_answer FROM TasksAnswers WHERE task_id=?", (task_ident,))
            row = await cursor.fetchone()
            check_answ = row[0] if row else None

            cursor = await db.execute("""
                    SELECT T.type, T.score, T.level_id, L.module_name, T.question, T.content, L.level_name
                    FROM Tasks T LEFT JOIN Modules L ON (T.module_id=L.module_id)
                    JOIN Levels L ON T.level_id = L.level_id
                    WHERE T.task_id=?
                """, (task_ident,))
            task_row = await cursor.fetchone()
            type_task, score_change, level_id, module_name, question, content, level_name = task_row

            if check_answ:
                if int(user_answer) == int(check_answ):
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

            else:
                if is_voice:
                    user_answer = transcribe_voice_message(
                        user_answer)

                prompt = evaluation_prompt.format(
                    content=content,
                    question=question,
                    user_answer=user_answer,
                    level_name=level_name,
                    module_name=module_name,
                    type_question=type_task)

                response = gigachat.invoke([
                    SystemMessage(content=prompt)
                ])

                try:
                    content = response.content.strip()
                    if content.startswith('```json') and content.endswith('```'):
                        json_content = content[7:-3].strip()
                    else:
                        json_content = content

                    print(json_content)
                    result = json.loads(json_content)
                    score = result.get('score', 0)
                    max_score = result.get('max_score', 0)
                    explanation = result.get('explanation', "")

                    await db.execute("""UPDATE UserModules
                            SET score = score + ?
                            WHERE user_id = ? AND level_id = ?
                            """, (score, user_ident, level_id))

                    await db.commit()

                    return {"score": score, "max_score": max_score, "explanation": explanation}

                except Exception as parse_error:
                    logger.error(f"Error parsing GigaChat response: {parse_error}, raw={response.content}")
                    return {"error": "Invalid response from AI"}


    except Exception as e:
        logger.error(f"Error checking user answer: {e}")
        return False



