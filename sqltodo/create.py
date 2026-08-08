import sqlite3
import os

project = os.path.dirname(os.path.abspath(__file__))

connection = sqlite3.connect(os.path.join(project, "tasks.db"))
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        progress INTEGER DEFAULT 0
    )
"""
)

connection.commit()
connection.close()

print("Veritabani basariyla olusturuldu!")