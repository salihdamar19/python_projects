import sqlite3
import os
from flask import Flask, render_template, request, redirect, url_for, session

project = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.secret_key = "gizi_sifre"

def toggle(flag):
    if flag == 1:
        return 0
    else:
        return 1

def selectAll():
    connection = sqlite3.connect(os.path.join(project, "tasks.db"))
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tasks")
    response = cursor.fetchall()
    session["len"] = len(response)
    return response

@app.route("/")
def index():
    if not session.get("cookie"):
        message = "Durumu tiklayarak degistirin."
        color = "#3f81bf"
        session["cookie"] = True
    else:
        message = None
        color = None

    connection = sqlite3.connect(os.path.join(project, "tasks.db"))
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tasks")
    response = cursor.fetchall()

    if not message:
        message = session.pop("message", None)
        color = session.pop("color", None)
    return render_template("index.html", gorevler=response, message=message, renk=color)

@app.route("/add", methods=["POST"])
def add():
    task = request.form["task"]
    task_tuple = (task,)
    connection = sqlite3.connect(os.path.join(project, "tasks.db"))
    cursor = connection.cursor()
    if not task:
        session["message"] = "Gorev basligi bos birakilamaz!"
        session["color"] = "#d14141"
        return redirect(url_for("index"))

    cursor.execute("INSERT INTO tasks (title) VAlUES (?)", task_tuple)
    connection.commit()

    session["message"] = "Gorev basariyla eklendi."
    session["color"] = "#3f81bf"
    return redirect(url_for("index"))

@app.route("/toggle", methods= ["POST"])
def complete():
    task_id = int(request.form["id"])
    progress = int(request.form["progress"])
    progress = toggle(progress)
    connection = sqlite3.connect(os.path.join(project, "tasks.db"))
    cursor = connection.cursor()
    cursor.execute("UPDATE tasks SET progress = ? WHERE id = ?", (progress, task_id))
    connection.commit()
    session["message"] = "Gorev ilerlemesi guncellendi."
    session["color"] = "#C0ECC0"
    return redirect(url_for("index"))

@app.route("/del", methods=["POST"])
def delete():
    task_id = int(request.form["task"])
    response = selectAll()

    global search_flag
    search_flag = False
    for task in response:
        if task[0] == task_id:
            search_flag = True
    
    if search_flag == False:
        session["message"] = "Gecersiz ID!"
        session["color"] = "#d14141"
        return redirect(url_for("index"))

    connection = sqlite3.connect(os.path.join(project, "tasks.db"))
    cursor = connection.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    connection.commit()

    session["message"] = "Gorev basarilya silindi."
    session["color"] = "#d14141"
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=False)
