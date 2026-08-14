import os
from flask import Flask, render_template, session, redirect, url_for, request
from dotenv import load_dotenv
import create
import random
import time
import requests

project = os.path.dirname(os.path.abspath(__file__))

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
brevo_key = os.getenv("BREVO_API_KEY")

@app.route("/", methods=["POST", "GET"])
def index():
    
    message = session.pop("message", None)
    return render_template("index.html", message=message)

@app.route("/signin", methods=["POST"])
def signin():
    email = request.form["email"]
    password = request.form["password"]
    users = create.selecALL()

    for user in users:
        if user[2] == email:
            if user[3] == password:
                session["message"] = "Giris Basarili"
                return redirect(url_for("index"))

    session["message"] = "Gecersiz kullanici adi veya sifre."
    return redirect(url_for("index"))


@app.route("/signup", methods=["POST"])
def signup():
    session["fullName"] = request.form["fullName"]
    session["email"] = request.form["email"]
    session["password"] = request.form["password"]

    users = create.selecALL()

    for user in users:
        if user[2] == session.get("email"):
           session["message"]="Bu eposta kayitli lutfen giris yapin!"
           return redirect(url_for("index"))
        
    session["message"] = create.insert(session.get("fullName"), session.get("email"), session.get("password"))
    
    return redirect(url_for("index"))

@app.route("/send", methods=["POST"])
def send():
    session["kod"] = random.randint(100000,999999)
    session["email"] = request.form["email"]

    session["users"] = create.selecALL()
    session["userFlag"] = False
    for user in session.get("users"):
        if user[2] == session.get("email"):
            session["userFlag"] = True
    if session.get("userFlag") == False:
        return render_template("index.html", action="/send", message="Lutfen once hesap olusturunuz.")

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
        session["message"] = f"Bir hata olustu luften daha sonra tekrar deneyin{str(e)}"
        return redirect(url_for("index"))
    session["code_count"] = 0
    session["message"] = "6 haneli dogrulama kodu gonderildi."
    message = session.get("message")
    return render_template("index.html", action="/verify", message=message)

@app.route("/verify", methods=["POST", "GET"])
def verify():
    session["code_count"] += 1
    session["user_code"] = int(request.form["code"])
    if session.get("kod") == session.get("user_code"):
        session["message"] = "Kod dogru yonlenriliyorsunuz."
        return redirect(url_for("index"))
    elif session.get("code_count") == 3:
        session["message"] = "3 kez yanlis kod girdiniz lutfen yeni kod talep edin."
        return render_template("index.html", action="/verify", message=session.get("message"))
    else:
        session["message"] = "Yanlis kod."
        return render_template("index", action="/verify",message=session.get("message"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")