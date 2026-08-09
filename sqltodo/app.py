import sqlite3
import os
from flask import Flask, render_template, request

project = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


@app.route("/")
def index():
    connection = sqlite3.connect(os.path.join(project, "tasks.db"))
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tasks")
    response = cursor.fetchall()
    return render_template("index.html", gorevler=response)

@app.route("/add", methods=["POST"])
def add():
    task = request.form["task"]
    task_tuple = (task,)
    connection = sqlite3.connect(os.path.join(project, "tasks.db"))
    cursor = connection.cursor()
    if not task:
        cursor.execute("SELECT * FROM tasks")
        response = cursor.fetchall()
        return render_template("index.html", message="Gorev basligi bos birakilamaz.", gorevler=response)

    cursor.execute("INSERT INTO tasks (title) VAlUES (?)", task_tuple)
    connection.commit()
    cursor.execute("SELECT * FROM tasks")
    response = cursor.fetchall()
    return render_template("index.html", message="Gorev basariyla eklendi.", gorevler=response)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")