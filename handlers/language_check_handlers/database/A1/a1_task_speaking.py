import sqlite3

db = sqlite3.connect('BFU')
cursor = db.cursor()

def add_new_task_optional(level_score, level_name, module_name, type_task, task_content, task_question, task_score, check_method, answer):

    cursor.execute("SELECT level_id FROM Levels where level_name=?", (level_name, ))
    row = cursor.fetchone()
    if row:
        level_id = row[0]
    else:
        cursor.execute("INSERT INTO Levels (level_score, level_name) VALUES(?, ?)",
               (level_score, level_name))
        level_id = cursor.lastrowid

    cursor.execute("SELECT module_id FROM Modules where module_name=?", (module_name, ))
    row = cursor.fetchone()
    if row:
        module_id = row[0]
    else:
        cursor.execute("INSERT INTO Modules(module_name) VALUES(?)", (module_name, ))
        module_id = cursor.lastrowid

    cursor.execute("SELECT 1 FROM LevelsModules WHERE level_id=? AND module_id=?", (level_id, module_id))
    if not cursor.fetchone():
        cursor.execute("INSERT INTO LevelsModules(level_id, module_id) VALUES(?, ?)", (level_id, module_id))

    cursor.execute("SELECT task_id FROM Tasks WHERE question=? AND content=?", (task_question, task_content))
    row = cursor.fetchone()
    if row:
        task_id = row[0]
    else:

        cursor.execute("INSERT INTO Tasks(module_id, type, content, question, score, check_method) VALUES(?, ?, ?, ?, ?, ?)",
               (module_id,
                type_task,
                task_content,
                task_question,
                task_score,
                check_method)
               )
        task_id = cursor.lastrowid

    cursor.execute("""
            INSERT INTO TasksAnswers (task_id, correct_answer)
            VALUES (?, ?, ?)
            """, (task_id, answer)
                   )
    db.commit()

def add_new_task(level_score, level_name, module_name, type_task, task_content, task_question, check_method, task_score):
    cursor.execute("SELECT level_id FROM Levels where level_name=?", (level_name,))
    row = cursor.fetchone()
    if row:
        level_id = row[0]
    else:
        cursor.execute("INSERT INTO Levels (level_score, level_name) VALUES(?, ?)",
               (level_score, level_name))
        level_id = cursor.lastrowid

    cursor.execute("SELECT module_id FROM Modules where module_name=?", (module_name,))
    row = cursor.fetchone()
    if row:
        module_id = row[0]
    else:
        cursor.execute("INSERT INTO Modules(module_name) VALUES(?)", (module_name,))
        module_id = cursor.lastrowid

    cursor.execute("SELECT 1 FROM LevelsModules WHERE level_id=? AND module_id=?", (level_id, module_id))
    if not cursor.fetchone():
        cursor.execute("INSERT INTO LevelsModules(level_id, module_id) VALUES(?, ?)", (level_id, module_id))

    cursor.execute("SELECT task_id FROM Tasks WHERE question=? AND content=?", (task_question, task_content))
    row = cursor.fetchone()
    if row:
        task_id = row[0]
    else:
        task_id = cursor.lastrowid
        cursor.execute("INSERT INTO Tasks(module_id, type, content, question, score, check_method) VALUES(?, ?, ?, ?, ?, ?)",
                       (module_id,
                        type_task,
                        task_content,
                        task_question,
                        task_score,
                        check_method)
                       )

    db.commit()

# Speaking

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Вам задали вопрос: «Как вы себя чувствуете?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Вам задали вопрос: «Скажите, пожалуйста, вы говорите по-английски?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Вам задали вопрос: «Сколько вам лет?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Вам задали вопрос: «Откуда вы?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Вам задали вопрос: «Вы студент или работаете?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Вам задали вопрос: «Как зовут вашу маму?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Вам задали вопрос: «Как зовут ваших родителей?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Вам задали вопрос: «Кто ваш лучший друг или подруга?» ',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Вам задали вопрос: «У вас много друзей?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Вам задали вопрос: «Ваши друзья живут далеко от вас?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Вам задали вопрос: «На каком языке говорит ваш лучший друг?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Вам задали вопрос: «Сегодня солнечно или идёт дождь?» ',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Вам задали вопрос: «Какая сегодня погода?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Вам задали вопрос: «В вашем городе часто снег зимой?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Вам задали вопрос: «Вы любите жару?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Вам задали вопрос: «Где вы учитесь?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Вам задали вопрос: «Вы учитесь или работаете?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Вам задали вопрос: «Вам нравится ваш университет?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Вам задали вопрос: «Вы любите читать книги?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Вам задали вопрос: «Вы любите смотреть фильмы или сериалы?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Вам задали вопрос: «Вы любите ездить на поезде или на автобусе?» ',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Вы в автобусе. Слышите объявление:\n\n— Следующая остановка — «Центральный рынок».\n\n Вопрос: Куда вы приедете на следующей остановке?',
             'Ваша задача: Назвать место.\n\nОтветьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Вы покупаете билет в кино. Кассир спрашивает:\n\n — Один билет на «Мстители» на 19:00?\n\nВопрос: На какой фильм и во сколько билет?',
             'Ваша задача: Повторить ключевую информацию (фильм и время).\n\nОтветьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Ситуация: Вы в магазине. Продавец спрашивает:\n\n — Вам пакет нужен?',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Easy', 'Speaking',
             'Ситуация: Вы спросили, где банк. Прохожий ответил:\n\n— Банк там, рядом с аптекой.',
             'Вопрос: Где банк?\n\nОтветьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             5)

add_new_task(1, 'A1', 'Middle', 'Speaking',
             '',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             7)

add_new_task(1, 'A1', 'Middle', 'Speaking',
             'Вам задал вопрос друг: «Где вы обычно отдыхаете летом?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             7)

add_new_task(1, 'A1', 'Middle', 'Speaking',
             'Вам задали вопрос: «Где вы живёте?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             7)

add_new_task(1, 'A1', 'Middle', 'Speaking',
             'Вам задали вопрос: «Сколько у вас братьев и сестёр?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             7)

add_new_task(1, 'A1', 'Middle', 'Speaking',
             'Вам задали вопрос: «Есть ли у вас домашние животные?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             7)

add_new_task(1, 'A1', 'Middle', 'Speaking',
             'Вам задали вопрос: «Сколько человек в вашей семье?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             7)

add_new_task(1, 'A1', 'Middle', 'Speaking',
             'Вам задали вопрос: «Где живёт ваша семья?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             7)

add_new_task(1, 'A1', 'Middle', 'Speaking',
             'Вам задали вопрос: «Вы часто видитесь с семьёй?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             7)

add_new_task(1, 'A1', 'Middle', 'Speaking',
             'Вам задали вопрос: «Ваш друг тоже изучает русский язык?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             7)

add_new_task(1, 'A1', 'Middle', 'Speaking',
             'Вам задали вопрос: «Как часто вы звоните друзьям?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             7)

add_new_task(1, 'A1', 'Middle', 'Speaking',
             'Вам задали вопрос: «Вы смотрите прогноз погоды?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             7)

add_new_task(1, 'A1', 'Middle', 'Speaking',
             'Вам задали вопрос: «Вы берёте зонт, если по прогнозу дождь?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             7)

add_new_task(1, 'A1', 'Middle', 'Speaking',
             'Вам задали вопрос: «Во сколько начинается ваш учебный день?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             7)

add_new_task(1, 'A1', 'Middle', 'Speaking',
             'Вам задали вопрос: «Вы устаёте после учебы?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             7)

add_new_task(1, 'A1', 'Middle', 'Speaking',
             'Вам задали вопрос: «Какое у вас хобби?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             7)

add_new_task(1, 'A1', 'Middle', 'Speaking',
             'Вам задали вопрос: «Какой сегодня день недели?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             7)

add_new_task(1, 'A1', 'Middle', 'Speaking',
             'Вам задали вопрос: «Когда у вас день рождения?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             7)

add_new_task(1, 'A1', 'Middle', 'Speaking',
             'Вам задали вопрос: «В каком месяце вы родились?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             7)

add_new_task(1, 'A1', 'Middle', 'Speaking',
             'Вам задали вопрос: «Сколько дней в неделе?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             7)

add_new_task(1, 'A1', 'Middle', 'Speaking',
             'Ситуация: Вы в кафе. Официант спрашивает:\n\n— Что будете пить?',
             'Ваша задача: Назвать напиток.\n\nОтветьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             7)

add_new_task(1, 'A1', 'Senior', 'Speaking',
             'Вам задали вопрос: «О чём вы мечтаете?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             10)

add_new_task(1, 'A1', 'Senior', 'Speaking',
             'Вам задали вопрос: «Кто в вашей семье самый старший?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             10)

add_new_task(1, 'A1', 'Senior', 'Speaking',
             'Вам задали вопрос: «Что вы любите делать вместе с семьёй?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             10)

add_new_task(1, 'A1', 'Senior', 'Speaking',
             'Вам задали вопрос: «Где вы познакомились с вашим лучшим другом?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             10)

add_new_task(1, 'A1', 'Senior', 'Speaking',
             'Вам задали вопрос: «Как вы проводите время с друзьями?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             10)

add_new_task(1, 'A1', 'Senior', 'Speaking',
             'Вам задали вопрос: «Что вам нравится в вашем друге?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             10)

add_new_task(1, 'A1', 'Senior', 'Speaking',
             'Вам задали вопрос: «Какая ваша любимая погода?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             10)

add_new_task(1, 'A1', 'Senior', 'Speaking',
             'Вам задали вопрос: «Что вы делаете, когда идёт дождь?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             10)

add_new_task(1, 'A1', 'Senior', 'Speaking',
             'Вам задали вопрос: «Какая погода была вчера?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             10)

add_new_task(1, 'A1', 'Senior', 'Speaking',
             'Вам задали вопрос: «На кого вы учитесь?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             10)

add_new_task(1, 'A1', 'Senior', 'Speaking',
             'Вам задали вопрос: «Кем вы хотите работать?» ',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             10)

add_new_task(1, 'A1', 'Senior', 'Speaking',
             'Вам задали вопрос: «С кем вы обычно проводите выходные?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             10)

add_new_task(1, 'A1', 'Senior', 'Speaking',
             'Вам задали вопрос: «Где вы обычно отдыхаете летом?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             10)

add_new_task(1, 'A1', 'Senior', 'Speaking',
             'Вам задали вопрос: «Который сейчас час?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             10)

add_new_task(1, 'A1', 'Senior', 'Speaking',
             'Вам задали вопрос: «Какое сегодня число?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             10)

add_new_task(1, 'A1', 'Senior', 'Speaking',
             'Вам задали вопрос: «Во сколько вы обычно просыпаетесь?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             10)

add_new_task(1, 'A1', 'Senior', 'Speaking',
             'Вам задали вопрос: «Сколько времени вы тратите на дорогу до работы/университета?»',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             10)

add_new_task(1, 'A1', 'Senior', 'Speaking',
             'Вы звоните в такси. Диспетчер спрашивает:\n\n— Какой ваш адрес? Откуда вас забрать?\n\nВаша задача: Назвать свой адрес или любое место в городе.',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             10)

add_new_task(1, 'A1', 'Senior', 'Speaking',
             'Вы встречаете друга в аэропорту. Он звонит и говорит:\n\n— Я прилетел! Я выхожу к выходу номер 3.\n\nЗадание: Ответьте другу, что скоро подойдете, и скажите, где вы находитесь (можете придумать номер выхода). ',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             10)

add_new_task(1, 'A1', 'Senior', 'Speaking',
             'Вы договорились встретиться с другом у торгового центра. Он пришел первым и звонит вам:\n\n — Я уже у торгового центра. Где ты?\n\nЗадание: Ответьте, что вы скоро, и назовите свое текущее место (можно выдумать).',
             'Ответьте (отправьте голосовое сообщение).',
             'open_question_speaking',
             10)