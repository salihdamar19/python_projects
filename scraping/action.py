import requests
from bs4 import BeautifulSoup

s = requests.session()

url = "http://quotes.toscrape.com/login"

login_page = s.get(url)
soup = BeautifulSoup(login_page.text, "html.parser")
csrf_token = soup.find("input", {"name" : "csrf_token"})["value"]

s.post(url, data={
    "csrf_token" : csrf_token,
    "username" : "test",
    "password" : "12345"
})

anasayfa = s.get("http://quotes.toscrape.com/")
if "Logout" in anasayfa.text:
    print('Giris basarili')
else:
    print('Giris basarisiz')

import os
folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder, "index.html")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(anasayfa.text)