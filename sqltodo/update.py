import sqlite3
import os

project = os.path.dirname(os.path.abspath(__file__))

connection = sqlite3.connect(os.path.join(project, "tasks.db"))
cursor = connection.cursor()

cursor.execute("UPDATE tasks SET progress = ? WHERE id = ?", (1,1))
connection.commit()
connection.close()