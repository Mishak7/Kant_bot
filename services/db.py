import sqlite3

db = sqlite3.connect('BFU')
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Levels (
level_id INTEGER PRIMARY KEY AUTOINCREMENT,
level_score INTEGER,
level_name TEXT
)
"""
)

cursor.execute("""
CREATE TABLE IF NOT EXISTS Modules (
module_id INTEGER PRIMARY KEY AUTOINCREMENT, 
module_name TEXT
)
"""
)

cursor.execute("""
CREATE TABLE IF NOT EXISTS LevelsModules(
level_id INTEGER, 
module_id INTEGER, 
FOREIGN KEY(level_id) REFERENCES Levels(level_id),
FOREIGN KEY(module_id) REFERENCES Modules(module_id), 
PRIMARY KEY (level_id, module_id)
)
"""
)

cursor.execute("""
CREATE TABLE IF NOT EXISTS Tasks(
task_id INTEGER PRIMARY KEY AUTOINCREMENT, 
level_id INTEGER, 
type TEXT NOT NULL,
content TEXT NOT NULL, 
question TEXT NOT NULL, 
score INTEGER DEFAULT 10,
FOREIGN KEY(level_id) REFERENCES Levels(level_id)
)
"""
)

cursor.execute("""
CREATE TABLE IF NOT EXISTS TasksAnswers(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
task_id INTEGER, 
correct_answer INTEGER, 
FOREIGN KEY(task_id) REFERENCES Tasks(task_id)
)
"""
)

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
telegram_id BIGINT UNIQUE NOT NULL, 
username TEXT, 
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""
)

# изменила module_id на level_id (чтобы мы сохраняли именно прогресс по уровню, а не easy и тд модулям
cursor.execute("""
CREATE TABLE IF NOT EXISTS UserModules(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
user_id INTEGER, 
level_id INTEGER,
level_name TEXT,
score INTEGER DEFAULT 0, 
is_completed BOOLEAN DEFAULT FALSE, 
completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
FOREIGN KEY(user_id) REFERENCES Users(id), 
FOREIGN KEY(level_id) REFERENCES Levels(level_id),
FOREIGN KEY(level_name) REFERENCES Levels(level_name)
)
"""
)

cursor.execute("""
CREATE TABLE IF NOT EXISTS UserProgress(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
user_id INTEGER, 
task_id INTEGER, 
user_answer TEXT, 
is_correct BOOLEAN NOT NULL, 
score_earned INTEGER, 
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
FOREIGN KEY(user_id) REFERENCES Users(id), 
FOREIGN KEY(task_id) REFERENCES Tasks(task_id)
)
"""
)

db.commit()

cursor.execute("PRAGMA table_info(Tasks)")
columns = [col[1] for col in cursor.fetchall()]

if "check_method" not in columns:
    cursor.execute("ALTER TABLE Tasks ADD COLUMN check_method TEXT")
else:
    print("Столбец уже существует")

db.commit()

res = cursor.execute("SELECT * from Modules")
print(res.fetchall())