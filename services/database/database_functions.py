import aiosqlite
import os
from config.logger import logger
from typing import Optional
from langchain_gigachat.chat_models import GigaChat
from langchain_core.messages import SystemMessage
from services.database.database_prompts.evaluation_prompt import evaluation_prompt
from services.database.database_prompts.explanation_prompt import explanation_prompt
from services.database.database_prompts.hint_prompt import hint_prompt
from services.database.speech_utils import transcribe_voice_message, text_to_speech
from config.settings import Settings
import json
from aiogram.types import FSInputFile
import random

# ОЧЕНЬ ВРЕМЕННО - спрятать такое лучше
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
    with_audio=False,
    update_existing=False
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
        with_audio=False,
        update_existing=False
    ):
        async with db.cursor() as cursor:
            await cursor.execute("SELECT level_id FROM Levels WHERE level_name=? AND level_score=?",
                               (level_name, level_score))
            row = await cursor.fetchone()
            if row:
                level_id = row[0]
            else:
                await cursor.execute("INSERT INTO Levels (level_score, level_name) VALUES(?, ?)",
                                   (level_score, level_name))
                level_id = cursor.lastrowid
                logger.info(f"Добавлен новый уровень: {level_name} (score: {level_score})")

            await cursor.execute("SELECT module_id FROM Modules WHERE module_name=?", (module_name,))
            row = await cursor.fetchone()
            if row:
                module_id = row[0]
            else:
                await cursor.execute("INSERT INTO Modules (module_name) VALUES(?)", (module_name,))
                module_id = cursor.lastrowid
                logger.info(f"Добавлен новый модуль: {module_name}")

            await cursor.execute("SELECT 1 FROM LevelsModules WHERE level_id=? AND module_id=?", (level_id, module_id))
            if not await cursor.fetchone():
                await cursor.execute("INSERT INTO LevelsModules(level_id, module_id) VALUES(?, ?)",
                                   (level_id, module_id))
                logger.info(f"Добавлена связь: уровень {level_name} - модуль {module_name}")

            await cursor.execute("""
                SELECT task_id FROM Tasks
                WHERE level_id=? AND module_id=? AND type=? AND question=? AND check_method=?
            """, (level_id, module_id, type_task, task_question, check_method))
            row = await cursor.fetchone()
            if not row:
                # Добавление нового задания
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
                if answer is not None:
                    await cursor.execute("""
                        INSERT INTO TasksAnswers (task_id, correct_answer)
                        VALUES (?, ?)
                    """, (task_id, answer))
                logger.info(f"Добавлено новое задание: {task_question}")
            else:
                task_id = row[0]
                if update_existing:
                    await cursor.execute("SELECT content FROM Tasks WHERE task_id=?", (task_id,))
                    current_content = await cursor.fetchone()
                    content_changed = not current_content or current_content[0] != task_content

                    if content_changed:
                        if with_audio:
                            audio_path = text_to_speech(task_content, "temp.wav")
                            with open(audio_path, "rb") as f:
                                audio_blob = f.read()
                            await cursor.execute("""
                                UPDATE Tasks
                                SET content=?, score=?, check_method=?, audio=?
                                WHERE task_id=?
                            """, (task_content, task_score, check_method, audio_blob, task_id))
                            if os.path.exists(audio_path):
                                os.remove(audio_path)
                        else:
                            await cursor.execute("""
                                UPDATE Tasks
                                SET content=?, score=?, check_method=?
                                WHERE task_id=?
                            """, (task_content, task_score, check_method, task_id))
                    else:
                        await cursor.execute("""
                            UPDATE Tasks
                            SET score=?, check_method=?
                            WHERE task_id=?
                        """, (task_score, check_method, task_id))

                    if answer is not None:
                        await cursor.execute("SELECT id FROM TasksAnswers WHERE task_id=?", (task_id,))
                        existing_answer = await cursor.fetchone()
                        if existing_answer:
                            await cursor.execute("""
                                UPDATE TasksAnswers
                                SET correct_answer=?
                                WHERE task_id=?
                            """, (answer, task_id))
                        else:
                            await cursor.execute("""
                                INSERT INTO TasksAnswers (task_id, correct_answer)
                                VALUES (?, ?)
                            """, (task_id, answer))
                    logger.info(f"Обновлено существующее задание: {task_question}")
                else:
                    logger.info(f"Задание уже существует (пропущено): {task_question}")
            await db.commit()

    async with aiosqlite.connect('BFU.db') as db:
        if data is not None:
            tasks = data.get("tasks", [])
            logger.info(f"Начало обработки {len(tasks)} заданий")
            for i, task in enumerate(tasks, 1):
                logger.info(f"Обработка задания {i}/{len(tasks)}: {task.get('task_question', 'No question')}")
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
                    with_audio=task.get("with_audio", False),
                    update_existing=update_existing
                )
            logger.info("Все задания обработаны")
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
                with_audio=with_audio,
                update_existing=update_existing
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
            cursor = await db.execute("SELECT level_id FROM Levels WHERE level_name = ?", (name_level,))
            level_row = await cursor.fetchone()
            level_id = level_row[0] if level_row else None

            cursor = await db.execute("SELECT score FROM UserModules WHERE user_id = ? AND level_id=?",
                                      (user_id, level_id))
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
                """SELECT T.task_id, T.content, T.type, T.question, T.audio FROM Tasks T
                WHERE T.module_id =? AND T.level_id = ? 
                AND T.task_id NOT IN(
                    SELECT task_id FROM UserProgress
                    WHERE user_id = ? and is_correct=TRUE)
                ORDER BY RANDOM() 
                LIMIT 1
                """,
                (module_id, level_id, user_id))
            row = await cursor.fetchone()
            await update_user_progress(user_id, row[0])
            return row

    except Exception as e:
        logger.error(f"Error getting a task: {e}")
        return False


async def review_mistakes(user_id, level):
    """
    Функция, которая позволяет пользователю после прохождения всего уровня перепройти невыполненные или плохо выполненные задания.
    """
    try:
        async with aiosqlite.connect('BFU.db') as db:
            cursor = await db.execute("SELECT level_id FROM Levels WHERE level_name = ?", (level,))
            level_row = await cursor.fetchone()
            level_id = level_row[0] if level_row else None

            cursor = await db.execute("SELECT task_id FROM UserProgress WHERE user_id = ? AND is_correct = ?",
                                      (user_id, False))
            unfinished_tasks = await cursor.fetchall()
            if not unfinished_tasks:
                return None

            random_task_id = random.choice([task[0] for task in unfinished_tasks])

            cursor = await db.execute(
                """SELECT T.task_id, T.content, T.type, T.question, T.audio FROM Tasks T
                WHERE T.task_id = ? AND T.level_id = ?
                """,
                (random_task_id, level_id))
            row = await cursor.fetchone()
            return row

    except Exception as e:
        logger.error(f"Error getting a review task: {e}")
        return False


async def all_tasks_done_right(user_id, level):
    """
    Функция, которая показывает, если пользователь правильно прошел все задания одного модуля
    """
    try:
        async with aiosqlite.connect('BFU.db') as db:
            cursor = await db.execute("SELECT level_id FROM Levels WHERE level_name = ?", (level,))
            level_row = await cursor.fetchone()
            level_id = level_row[0] if level_row else None

            cursor = await db.execute(
                "SELECT COUNT(DISTINCT task_id) FROM UserProgress WHERE user_id = ? AND is_correct = ?",
                (user_id, True))
            done_right_tasks = (await cursor.fetchone())[0]

            cursor = await db.execute("SELECT COUNT (*) FROM Tasks WHERE level_id = ?", (level_id,))
            all_tasks = (await cursor.fetchone())[0]

            return done_right_tasks == all_tasks

    except Exception as e:
        logger.error(f"Error function all_task_done_right: {e}")
        return False


async def all_tasks_done(user_id, level):
    """
    Функция, которая показывает, если пользователь прошел все задания одного модуля
    """
    try:
        async with aiosqlite.connect('BFU.db') as db:
            cursor = await db.execute("SELECT level_id FROM Levels WHERE level_name = ?", (level,))
            level_row = await cursor.fetchone()
            level_id = level_row[0] if level_row else None

            cursor = await db.execute("SELECT COUNT(DISTINCT task_id) FROM UserProgress WHERE user_id = ?", (user_id,))
            done_tasks = (await cursor.fetchone())[0]

            cursor = await db.execute("SELECT COUNT (*) FROM Tasks WHERE level_id = ?", (level_id,))
            all_tasks = (await cursor.fetchone())[0]

            return done_tasks == all_tasks

    except Exception as e:
        logger.error(f"Error function all_task_done: {e}")
        return False


async def prepare_question(task):
    """
    Функция prepare_question формирует в удобном ответе результат выбора рандомного задания из бд.

    task - результат работы функции get_task.
    """
    task_id, content, task_type, question, audio = task
    # в выводе задания пользователю мы выводим только question, audio
    # content, task_id нам нужны доя проверки
    if audio:
        return {"task_id": task_id, "content": content, "type": task_type, "question": question, "audio": audio}
    else:
        return {"task_id": task_id, "content": content, "type": task_type, "question": question}


async def extract_audio_from_db(task_id: str) -> Optional[FSInputFile]:
    """
    Функция для извлечения аудио из бд.
    Если файл уже существует - возвращает его, иначе создает новый.
    """
    audio_path = f"extracted_audio_listening/extracted_audio_{task_id}.mp3"

    if os.path.exists(audio_path):
        return FSInputFile(audio_path)

    else:
        async with aiosqlite.connect('BFU.db') as db:
            cursor = await db.execute("SELECT audio FROM Tasks WHERE task_id=?", (task_id,))
            row = await cursor.fetchone()

        if row and row[0]:
            audio_blob = row[0]
            with open(audio_path, "wb") as f:
                f.write(audio_blob)
            return FSInputFile(audio_path)
        else:
            return None


async def update_user_score(user_ident, level_id, score_change):
    try:
        async with aiosqlite.connect('BFU.db') as db:
            result = await db.execute(
                "SELECT score FROM UserModules WHERE user_id=? AND level_id=?",
                (user_ident, level_id))
            score = await result.fetchone()
            if score:
                if score[0] < 100:
                    await db.execute(
                        "UPDATE UserModules SET score = score + ? WHERE user_id = ? AND level_id = ?",
                        (score_change, user_ident, level_id))

                    await db.execute(
                        "UPDATE Users SET score = score + ? WHERE id = ?",
                        (score_change, user_ident)
                    )

                else:
                    await db.execute(
                        "UPDATE UserModules SET is_completed = 1, completed_at = CURRENT_TIMESTAMP WHERE user_id = ? AND level_id = ?",
                        (score_change, user_ident, level_id)
                    )

                    await db.execute(
                        "UPDATE Users SET score = score + ? WHERE id = ?",
                        (score_change, user_ident)
                    )

            else:
                await db.execute(
                    "INSERT INTO UserModules (user_id, level_id, score) VALUES (?, ?, ?)",
                    (user_ident, level_id, score_change))
            await db.commit()
            return None
    except Exception as e:
        logger.error(f"Error connecting to db: {e}")
        return False


async def update_user_progress(user_ident, task_ident, correct=False):
    try:
        async with aiosqlite.connect('BFU.db') as db:
            result = await db.execute(
                "SELECT task_id FROM UserProgress WHERE user_id=? AND task_id=?",
                (user_ident, task_ident))
            if await result.fetchone():
                await db.execute(
                    "UPDATE UserProgress SET is_correct=? WHERE user_id=? AND task_id=?",
                    (correct, user_ident, task_ident)
                )
            else:
                await db.execute(
                    "INSERT INTO UserProgress (user_id, task_id, is_correct) VALUES (?, ?, ?)",
                    (user_ident, task_ident, correct)
                )

            await db.commit()

    except Exception as e:
        logger.error(f"Error connecting to db: {e}")
        return False


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
                    SELECT T.type, T.score, T.level_id, M.module_name, T.question, T.content, L.level_name
                    FROM Tasks T LEFT JOIN Modules M ON (T.module_id=M.module_id)
                    JOIN Levels L ON T.level_id = L.level_id
                    WHERE T.task_id=?
                """, (task_ident,))
            task_row = await cursor.fetchone()
            type_task, score_change, level_id, module_name, question, content, level_name = task_row

            if check_answ:
                if int(user_answer) == int(check_answ):
                    await update_user_score(user_ident, level_id, score_change)
                    correct = True
                    multiple_choice_response = f'верно!За это задание вы набрали: {score_change}'
                else:
                    correct = False
                    multiple_choice_response = 'неверно'
                await update_user_progress(user_ident, task_ident, correct)
                return multiple_choice_response

            else:
                if is_voice:
                    user_answer = transcribe_voice_message(
                        user_answer)

                prompt = evaluation_prompt.format(
                    content=content,
                    question=question,
                    user_answer=user_answer,
                    level_name=level_name,
                    score=score_change,
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

                    await update_user_score(user_ident, level_id, int(score))

                    if score == 0.7 * max_score:
                        correct = True
                    else:
                        correct = False

                    await update_user_progress(user_ident, task_ident, correct)

                    return {"score": score, "max_score": max_score, "explanation": explanation}

                except Exception as parse_error:
                    logger.error(f"Error parsing GigaChat response: {parse_error}, raw={response.content}")
                    return {"error": "Invalid response from AI"}

    except Exception as e:
        logger.error(f"Error checking user answer: {e}")
        return False


async def explain_multiple_choice(task_ident, user_answer):
    try:
        async with aiosqlite.connect('BFU.db') as db:
            cursor = await db.execute("SELECT correct_answer FROM TasksAnswers WHERE task_id=?", (task_ident,))
            row = await cursor.fetchone()
            check_answ = row[0] if row else None

            cursor = await db.execute("""
                        SELECT T.question, T.content, L.level_name
                        FROM Tasks T
                        JOIN Levels L ON T.level_id = L.level_id
                        WHERE T.task_id = ?
                   """, (task_ident,))
            task_row = await cursor.fetchone()
            question, content, level_name = task_row

            explain = explanation_prompt.format(
                content=content,
                question=question,
                user_answer=user_answer,
                correct_answer=check_answ,
                level_name=level_name
            )
            response = gigachat.invoke([
                SystemMessage(content=explain)
            ])

            try:
                content = response.content.strip()

                return content

            except Exception as parse_error:
                logger.error(f"Error parsing GigaChat response: {parse_error}, raw={response.content}")
                return {"error": "Invalid response from AI"}

    except Exception as e:
        logger.error(f"Error checking user answer: {e}")
        return False


async def write_user_progress(user_id: int,
                              task_id: int,
                              user_answer: str,
                              is_correct: bool,
                              score_earned: int):
    async with aiosqlite.connect('BFU.db') as db:
        await db.execute("""
        INSERT INTO UserProgress (user_id, task_id, user_answer, is_correct, created_at)
        VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)""",
                         (user_id,
                          task_id,
                          user_answer,
                          is_correct,
                          score_earned,
                          ))
        await db.commit()


async def show_progress(user_ident, level_name):
    async with aiosqlite.connect('BFU.db') as db:
        cursor = await db.execute("""SELECT Levels.level_name, score 
                                  FROM UserModules LEFT JOIN Levels ON UserModules.level_id = Levels.level_id
                                  WHERE user_id=? AND Levels.level_name=?""", (user_ident, level_name))
        user_progress = await cursor.fetchone()
        level_name, score = user_progress
        return {'score': score,
                'level_name': level_name,
                'text': f"Ваш прогресс по уровню {level_name}: {min(score, 100)} / 100 баллов."}


async def give_hint(task_id):
    try:
        async with aiosqlite.connect('BFU.db') as db:
            cursor = await db.execute("SELECT content, question, level_name FROM Tasks LEFT JOIN Levels on Tasks.level_id = Levels.level_id WHERE task_id=?", (task_id,))
            content, question, level_name = await cursor.fetchone()

            cursor = await db.execute("""
            SELECT correct_answer 
            FROM TasksAnswers WHERE task_id=?
            """, (task_id,))
            result = await cursor.fetchone()

            answer = result[0] if result else None

            hint = hint_prompt.format(
                content=content,
                question=question,
                answer=answer,
                level_name=level_name
            )

            response = gigachat.invoke([
                SystemMessage(content=hint)])
            return response.content
    except Exception as e:
        logger.error(f"Error giving a hint: {e}")
        return False


async def select_leaders_from_leaderboard():
    try:
        async with aiosqlite.connect('BFU.db') as db:
            cursor = await db.execute("""SELECT username, score FROM Users
                                        ORDER BY score DESC
                                        LIMIT 5""")
            best_users = await cursor.fetchall()

            medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]
            lines_output = []

            for i, (user, score) in enumerate(best_users):
                medal = medals[i]
                lines_output.append(f'{medal} {user} - {score} баллов')

            final_leaderboard = '🏆Рейтинг лучших игроков:\n\n' + '\n'.join(lines_output)
            return final_leaderboard


    except Exception as e:
        logger.error(f"Error with showing leaderboard: {e}")
        return False


