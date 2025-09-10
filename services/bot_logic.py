# авторизация

import sqlite3

db = sqlite3.connect('BFU')
cursor = db.cursor()

# при авторизации получаем telegram_id и username пользователя
def get_user_id(inserted_telegram_id, inserted_username):
    cursor.execute("SELECT id FROM Users WHERE telegram_id = ?", (inserted_telegram_id,))
    user = cursor.fetchone()
    if user:
        return user[0]
    else:
        cursor.execute("INSERT INTO Users(telegram_id, username)", (inserted_telegram_id, inserted_username))
        return cursor.lastrowid

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