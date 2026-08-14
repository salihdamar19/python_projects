import sqlite3
import os

project = os.path.dirname(os.path.abspath(__file__))


def connectSQL():
    connection = sqlite3.connect(os.path.join(project, "users.db"))
    return connection

def connectANDcreateTable():
    connection = connectSQL()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        userID INTEGER PRIMARY KEY AUTOINCREMENT,
        fullName TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    """)

def selecALL():
    cursor = connectSQL().cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def insert(fullName, email, password):
    connetion = connectSQL()
    cursor = connetion.cursor()
    cursor.execute("INSERT INTO users (fullName, email, password) VALUES (?,?,?)", (fullName, email, password))
    connetion.commit()
    message = f"Aramiza hos geldin {fullName}"
    return message