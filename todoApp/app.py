import os
import tools
from flask import Flask, redirect, render_template, session, request, url_for
from dotenv import load_dotenv
import random
import time
import requests

project = os.path.dirname(os.path.abspath(__file__))

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
brevo_key = os.getenv("BREVO_API_KEY")

@app.route("/")
def index():
    message = session.pop("message", None)
    return render_template("index.html", message=message)

@app.route("/signin", methods=["POST"])
def signin():
    session["email"] = request.form["email"]
    session["password"] = request.form["password"]
    session["message"] = tools.signUser(session.get("email"), session.get("password"))
    session["color"] = '#C0ECC0'
    return redirect(url_for("tasks"))

@app.route("/signup", methods=["POST"])
def signup():
    session["fullName"] = request.form["fullName"]
    session["email"] = request.form["email"]
    session["password"] = request.form["password"]

    if tools.checkUserExistance(session.get("email")):
        session["message"] = "Bu kullanici zaten kayitli."
        return redirect(url_for("index"))

    session["message"] = tools.insertUSER(session.get("fullName"), session.get("email"), session.get("password"))
    return redirect(url_for("tasks"))

@app.route("/send", methods=["POST"])
def send():
    if session.get("next_send") and time.time() < session.get("next_send"):
        kalan = session.get("next_send") - time.time()
        return render_template("index.html", kalan_sure=kalan, action="/send") 
    
    session["code"] = random.randint(100000,999999)
    session["email"] = request.form["email"]

    if not tools.checkUserExistance(session.get("email")):
        return render_template("index.html", message="Lutfen once kayit olunuz.")

    url = "https://api.brevo.com/v3/smtp/email"
    headers = {
            "accept": "application/json",
            "api-key": brevo_key,
            "content-type": "application/json"
    }
    veri = {
                    "sender": {"name": "Dogrulama Sistemi", "email": "salihdamar612@gmail.com"},
            "to": [{"email":session.get("email")}],
            "subject": "Dogrulama Kodunuz",
            "textContent": f"Dogrulama Kodunuz<br>{session.get("kod")}"
    }
    try:
            requests.post(url, headers=headers, json=veri)
    except Exception as e:
            return render_template("index.html", action="/send", message=f"Bir hata olustu luften daha sonra tekrar deneyin{str(e)}")
    
    return render_template("index.html", action="/verify", message="6 haneli dogrulama kodu gonderildi.")

@app.route("/verify", methods=["POST", "GET"])
def verify():
    session["user_code"] = int(request.form["code"])
    if session.get("code") == session.get("user_code"):
        session["message"] = "Kod dogru yonlenriliyorsunuz."
        return redirect(url_for("tasks"))
    else:
        session["message"] = "Yanlis kod."
        return render_template("index", action="/verify",message=session.get("message"))

@app.route("/tasks")
def tasks():
    message = session.pop("message", None)
    color = session.pop("color", None)
    tasks = tools.selectTasks(session.get("email"))
    return render_template("tasks.html", tasks=tasks, message=message, color=color)

@app.route("/add", methods = ["POST"])
def add():
    task = request.form["task"]
    if not task:
        return redirect("tasks.html", message="Gorev basligi bos birakilamaz", color='#d14141')
    session["message"] = tools.insertTask(session.get("email"),task)
    session["color"] = "#3f81bf"
    return redirect(url_for("tasks"))

@app.route("/toggle", methods=["POST"])
def complete():
    task_id = int(request.form["id"])
    progress = int(request.form["progress"])
    if progress:
        progress = 0
    else:
        progress = 1
    session["message"] = tools.updateTask(session.get("email"), task_id, progress)
    session["color"] = '#C0ECC0'
    return redirect(url_for("tasks"))

@app.route("/del", methods=["POST"])
def delete():
    task_id = request.form["id"]
    session["message"] = tools.deleteTask(session.get("email"), task_id)
    session["color"] = '#d14141'
    return redirect(url_for("tasks"))

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")