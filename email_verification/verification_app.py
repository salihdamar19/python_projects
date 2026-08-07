from flask import Flask, session,  render_template, request, redirect, url_for
import os
from dotenv import load_dotenv
import random
import resend
import time
import requests


load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


resend.api_key = os.getenv("RESEND_API_KEY")
brevo_key = os.getenv("BREVO_API_KEY")


@app.route("/")
def anasayfa():
    return render_template("index.html")

@app.route("/uret", methods=["POST", "GET"])
def uret():
    if session.get("next_send") and session["next_send"] > time.time() :
        return render_template("dogrula.html", message=f"Lufen yeni kod icin {int(session.get("expire") - 240 - time.time())}sn bekleyiniz.")
    kod = random.randint(100000,999999)
    session["expire"] = time.time() + 300
    session["next_send"] = time.time() + 60
    session["kod"] = kod
    alici = request.form["email"]
    session["email"] = alici
    url = "https://api.brevo.com/v3/smtp/email"
    headers = {
        "accept": "application/json",
        "api-key": brevo_key,
        "content-type": "application/json"
    }
    veri = {
        "sender": {"name": "Dogrulama Sistemi", "email": "salihdamar612@gmail.com"},
        "to": [{"email":alici}],
        "subject": "Dogrulama Kodunuz",
        "textContent": f"Dogrulama Kodunuz<br>{kod}"
    }
    try:
        response = requests.post(url, headers=headers, json=veri)
        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)
        print("TUM FORM VERISI:", request.form)
        alici = request.form["email"]
        print("ALICI:", alici)
    except Exception as e:
        return f"Mail gonderilemedi: {e}"
        
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
        if time.time() > session["expire"]:
            return render_template("dogrula.html", message="Kodun Suresi Doldu")
        else:
            if request.form["kod"] == dogru_kod:
                session.pop("kod", None)
                session.pop("expire", None)
                session.pop("next_send", None)
                return render_template("dogrula.html", message="Kod Dogru")
            elif request.form["kod"]: 
                return render_template("dogrula.html", message="Kod Yanlis")
            else:
                render_template("dogrula.html", message="")
    return render_template("dogrula.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")