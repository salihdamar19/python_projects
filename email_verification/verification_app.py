from flask import Flask, session,  render_template, request, redirect, url_for
import os
from dotenv import load_dotenv
import random
import resend
import time

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")



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
    params = {
        "from" : "onboarding@resend.dev",
        "to": [alici],
        "subject" : "Dogrulama Kodu",
        "text": str(kod)
    }
    try:
        resend.Emails.send(params)
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