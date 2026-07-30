import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, request, url_for, session
import random

load_dotenv()
app = Flask(__name__)
app.secret_key = "herhangi_bir_gizli_metin_123"

email = os.getenv("EPOSTA_ADRESI")
password = os.getenv("EPOSTA_SIFRE")

@app.route("/", methods = ["GET", "POST"])
def anasayfa():
    if request.method == "POST":
        alici = request.form["mail"]
        key = random.randint(100000,999999)

        session["key"] = key
        session["alici"] = alici

        icerik = key

        mesaj = MIMEMultipart()
        mesaj["From"] = email
        mesaj["To"] = alici
        mesaj["Subject"] = "TEST"
        mesaj.attach(MIMEText(icerik, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as sunucu:
            sunucu.starttls()
            sunucu.login(alici, password)
            sunucu.send_message(mesaj)
        

@app.route("/dogrula", methods=["GET", "POST"])
def dogrula():
    if request.method == "POST":
        girilen_kod = request.form["kod"]
        dogru_kod = session.get("kod")
        if girilen_kod.isdigit() and int(girilen_kod) == dogru_kod:
            return "Giris Basarili"
        else:
            return "Kod yanlis tekrar dene."
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)



'''
for i in range(3):
    try:
        user_input = int(input('Dogrulama kodunu giriniz: '))
    except ValueError:
        print('Sayi gir')
    else:
        if user_input == x:
            print('Dogrulama kodu dogru! Yonlendiriyorsunuz...')
            break
        elif i == 2:
            print('3 kez yanlis kod girdiniz! Lutfen yeni kod aliniz.')
        else:
            print('Dogrulama kodu eksik veya yanlis')
            
'''


#print(x)


