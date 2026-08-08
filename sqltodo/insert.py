import sqlite3
import os

project = os.path.dirname(os.path.abspath(__file__))

connection = sqlite3.connect(os.path.join(project, "tasks.db"))  
cursor = connection.cursor()

cursor.execute("INSERT INTO tasks (title) VALUES (?)", ("Bulasik",))

connection.commit()
