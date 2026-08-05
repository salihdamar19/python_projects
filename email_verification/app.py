from flask import Flask, session,  render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
import random


app = Flask(__name__)
app.secret_key = "gizli_sifre_12345"
load_dotenv()

email = os.getenv("EPOSTA_ADRESI")
password = os.getenv("EPOSTA_SIFRE")



@app.route("/")
def anasayfa():
    return render_template("index.html")

@app.route("/uret", methods=["POST", "GET"])
def uret():
    kod = random.randint(100000,999999)
    session["kod"] = kod
    alici = request.form["email"]
    konu = "Dogrulama Kodu"
    mesaj = MIMEMultipart()
    mesaj["From"] = email
    mesaj["To"] = alici
    mesaj["Subject"] = konu
    mesaj.attach(MIMEText(str(kod), "plain"))
    with smtplib.SMTP("smtp.gmail.com", 587) as sunucu:
        sunucu.starttls()
        sunucu.login(email, password)
        sunucu.send_message(mesaj)
    return redirect(url_for("dogrula"))

@app.route("/arttir")
def arttir():
    if "sayac" not in session:
        session["sayac"] = 0
    session["sayac"] += 1
    return f"Sayac: {session["sayac"]}"

@app.route("/dogrula", methods=["POST", "GET"])
def dogrula():
    if request.method == "POST":
        dogru_kod = str(session.get("kod"))
        if request.form["kod"] == dogru_kod:
            return "Dogru kod."
        else:
            return "Yalnis kod"
    return render_template("dogrula.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")