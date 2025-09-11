# авторизация

import sqlite3
import aiosqlite
from config.logger import logger
from langchain_gigachat.chat_models import GigaChat
from langchain_core.messages import SystemMessage, HumanMessage
from handlers.language_check_handlers.database.prompts.prompt_check_writing import prompt as writing_prompt
from handlers.language_check_handlers.database.prompts.prompt_check_speaking import prompt as speaking_prompt
from handlers.language_check_handlers.database.prompts.prompt_check_listening import prompt as listening_prompt
from handlers.language_check_handlers.database.speech_utils import transcribe_voice_message

db = sqlite3.connect('BFU')
cursor = db.cursor()

gigachat = GigaChat(temperature = 0,
                    top_p = 0.1,
                    credentials=...,
                    verify_ssl_certificate=False)

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
    await cursor.execute("SELECT score FROM UserModules WHERE user_id = ? AND level_name=?", (user_id, name_level))
    row = await cursor.fetchone()
    user_score = row[0] if row else 0

    if user_score < 30:
        module_type = 'Easy'
    elif 30 <= user_score < 60:
        module_type = 'Middle'
    else:
        module_type = 'Senior'

    await cursor.execute("SELECT level_id FROM Levels WHERE level_name = ?", (name_level,))
    row = await cursor.fetchone()
    level_id = row[0] if row else None

    await cursor.execute("SELECT module_id FROM Modules WHERE module_name = ?", (module_type,))
    module = await cursor.fetchone()
    module_id = module[0] if module else None

    await cursor.execute("SELECT task_id, content, question FROM Tasks WHERE module_id =? AND level_id = ? ORDER BY RANDOM() LIMIT 1", (module_id, level_id))
    return await cursor.fetchone()


def prepare_question(task):
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


# тут дальше в коде мы получаем идентификтор из функции get_task
async def check_task(user_ident, task_ident, user_answer, is_voice=False):
    '''
    user_ident - идентификатор пользователя из get_user_id
    task_ident - идентификатор задания из get_task
    user_answer - ответ пользователя на задание, которое было выбрано в get_task
    is_voice - True если ответ юзера это голосовое (задание на спикинг)
    '''

    await cursor.execute("SELECT correct_answer FROM TasksAnswers WHERE task_id=?", (task_ident,))
    row = await cursor.fetchone()[0]
    check_answ = row[0] if row else None

    await cursor.execute("SELECT type, score, level_id FROM Tasks WHERE task_id=?", (task_ident,))
    task_row = await cursor.fetchone()
    type_task, score_change, level_id = task_row

    if check_answ:
        if user_answer == check_answ:
            await cursor.execute("""UPDATE UserModules 
                SET score = score + ? 
                WHERE user_id = ? AND level_id = ?
                """, (score_change, user_ident, level_id))
            return 'верно'
        else:
            await cursor.execute("""UPDATE UserModules
                SET score = score - ?
                WHERE user_id = ? AND level_id = ?
                """, (score_change, user_ident, level_id))
            await db.commit()
            return 'неверно' # тут нужно будет использовать эту функцию в самой логике работы, чтобы потом
            # ориентируясь на аутпут функции либо выводить объяснение правильного ответа с помощью гигачата + текущи скор
            # либо просто выводить а-ля "Вы молодец" и текущий скор
    else:

        if is_voice:
            user_answer = transcribe_voice_message(user_answer)

        if type_task == 'Speaking':
            prompt = speaking_prompt
        elif type_task == 'Listening':
            prompt = listening_prompt
        elif type_task == 'Writing':
            prompt = writing_prompt
        response = gigachat.invoke([
            HumanMessage(content=user_answer),
            SystemMessage(content=prompt)
        ])
        # здесь надо прописать, как очки добавлять, если открытый ответ (в промпте должно быть)
        return response.content