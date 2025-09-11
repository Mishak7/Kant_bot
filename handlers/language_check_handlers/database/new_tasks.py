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