import sqlite3
import os

project = os.path.dirname(os.path.abspath(__file__))

connection = sqlite3.connect(os.path.join(project, "tasks.db"))
cursor = connection.cursor()

cursor.execute("SELECT * FROM tasks")
response = cursor.fetchall()

print("id   baslik    0/1")
for row in response:
    print(row)