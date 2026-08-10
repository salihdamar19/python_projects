import sqlite3
import os
from flask import Flask, render_template, session, redirect, url_for, request
from dotenv import load_dotenv
import create

project = os.path.dirname(os.path.abspath(__file__))

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
brevo_key = os.getenv("BREVO_API_KEY")

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signin():
    email = request.form["email"]
    password = request.form["password"]
    users = create.selecALL()

    for user in users:
        if user[2] == email:
            if user[3] == password:
                return render_template("index.html", message="Giris Basarili")

    return render_template("index.html", message="Gecersiz kullanici adi veya sifre.")


@app.route("/signup", methods=["POST"])
def signup():
    fullName = request.form["fullName"]
    email = request.form["email"]
    password = request.form["password"]

    users = create.selecALL()

    for user in users:
        if user[2] == email:
            return render_template("index.html", message="Bu eposta kayitli lutfen giris yapin!")
    message = create.insert(fullName, email, password)
    return render_template("index.html", message=message)

@app.route("/forgot")
def forgot():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")