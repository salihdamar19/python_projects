import sqlite3
import os

project = os.path.dirname(os.path.abspath(__file__))

def connectSQL():
    connection = sqlite3.connect(os.path.join(project, "todo_app.db"))
    return connection

def createDB():
    connection = connectSQL()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
        userID INTEGER PRIMARY KEY AUTOINCREMENT,
        fullName TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INT NOT NULL,
        title TEXT NOT NULL,
        progress BIT NOT NULL DEFAULT 0,
        
        FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

def checkUserExistance(email):
    cursor = connectSQL().cursor()
    cursor.execute("SELECT email FROM users")
    user_mails = cursor.fetchall()

    for user_mail in user_mails:
        if user_mail == email:
            return True
    return False

def insertUSER(fullName, email, password):
    connection = connectSQL()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (fullName, email, password) VALUES (?,?,?)", (fullName, email, password))
    connection.commit()
    message = f"Aramiza hos geldin {fullName}"
    return message

def insertTask(email, title):
    connection = connectSQL()
    cursor = connection.cursor()
    cursor.execute("SELECT userID FROM users WHERE email = ?", (email,))
    user_id = cursor.fetchone()
    cursor.execute(
    "SELECT * FROM users")
    print(cursor.fetchall())
    cursor.execute("INSERT INTO tasks (user_id, title) VALUES (?,?)", (user_id[0], title))
    connection.commit()
    return "Gorev basariyla eklendi"

def selectTasks(email):
    cursor = connectSQL().cursor()
    cursor.execute("SELECT userID FROM users WHERE email = ?", (email,))
    user_id = cursor.fetchone()
    cursor.execute("SELECT * FROM tasks WHERE user_id = ?", (user_id[0],))
    tasks = cursor.fetchall()
    return tasks

def signUser(email, password):
    cursor = connectSQL().cursor()
    cursor.execute("SELECT email,password FROM users")
    users = cursor.fetchall()

    for user in users:
        if email == user[0]:
            if password == user[1]:
                return "Giris Basarili."
    return "Gecersiz kullanici adi veya sifre." 

def updateTask(email, task_id, progress):
    connection = connectSQL()
    cursor = connection.cursor()
    cursor.execute("SELECT userID FROM users WHERE email = ?", (email,))
    user_id = cursor.fetchone()
    cursor.execute("UPDATE tasks SET progress = ? WHERE id = ? AND user_id = ?", (progress, task_id, user_id[0]))
    connection.commit()
    return "Gorev ilerlemesi guncellendi."

def deleteTask(email, task_id):
    connection = connectSQL()
    cursor = connection.cursor()
    cursor.execute("SELECT userID FROM users WHERE email = ?", (email,))
    user_id = cursor.fetchone()
    try:
        cursor.execute("DELETE FROM tasks WHERE id = ? AND user_id = ?", 
        (task_id, user_id[0]))
        connection.commit()
    except Exception:
        return "Gecersiz ID."
    return "Gorev basariyla silindi."
