import aiosqlite
import os
from config.logger import logger
from typing import Optional


text_to_speech = lambda x: x

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




