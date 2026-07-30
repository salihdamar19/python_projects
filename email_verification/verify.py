import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
import random

load_dotenv()

email = os.getenv("EPOSTA_ADRESI")
password = os.getenv("EPOSTA_SIFRE")

alici = "salih1661@icloud.com"
konu = "Test"
x = random.randint(100000,999999)
icerik = f"{x}"


mesaj = MIMEMultipart()
mesaj["From"] = email
mesaj["To"] = alici
mesaj["Subject"] = konu
mesaj.attach(MIMEText(icerik, "plain"))

with smtplib.SMTP("smtp.gmail.com", 587) as sunucu:
    sunucu.starttls()
    sunucu.login(email, password)
    sunucu.send_message(mesaj)


for i in range(3):
    try:
        user_input = int(input('Dogrulama kodunu giriniz: '))
    except ValueError:
        print('Lutfen sayi giriniz: ')
    else:
        if user_input == x:
            print('Dogrulama kodu dogru! Yonlendiriyorsunuz...')
            break
        elif i == 2:
            print('3 kez yanlis kod girdiniz! Lutfen yeni kod aliniz.')
        else:
            print('Dogrulama kodu eksik veya yanlis')



#print(x)
