import os
from flask import Flask, render_template, session, redirect, url_for, request
from dotenv import load_dotenv
import create
import random
import time

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

@app.route("/forgot")
def forgot():
    session["kod"] = random.randint(100000,999999)
    session["email"] = request.form("email")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")