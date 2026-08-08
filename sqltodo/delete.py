import sqlite3
import os

project = os.path.dirname(os.path.abspath(__file__))

connection = sqlite3.connect(os.path.join(project, "tasks.db"))
cursor = connection.cursor()

cursor.execute("DELETE FROM tasks WHERE id = ? ", (2,))

connection.commit()
connection.close()