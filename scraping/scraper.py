import os
import requests
from bs4 import BeautifulSoup

folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder, "sozler.txt")

response = requests.get("http://quotes.toscrape.com/")
html = response.text

soup = BeautifulSoup(html, "html.parser")
sozler = soup.find_all("div", class_ = "quote")

with open(file_path, "a+", encoding="utf-8") as f:
    for soz in sozler:
        metin = soz.find("span", class_ = "text").text
        yazar = soz.find("small", class_ = "author").text
        print(f"{metin} - {yazar}")
        f.write(f'{metin} - {yazar}\n')