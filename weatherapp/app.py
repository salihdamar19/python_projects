import requests
import os
from flask import Flask, render_template, request, url_for
from dotenv import load_dotenv

ikon_eslesme = {
    "01d": "clear-day",
    "01n": "clear-night",
    "02d": "partly-cloudy-day",
    "02n": "partly-cloudy-night",
    "03d": "cloudy",
    "03n": "cloudy",
    "04d": "overcast",
    "04n": "overcast",
    "09d": "rain",
    "09n": "rain",
    "10d": "partly-cloudy-day-rain",
    "10n": "partly-cloudy-night-rain",
    "11d": "thunderstorms-day",
    "11n": "thunderstorms-night",
    "13d": "snow",
    "13n": "snow",
    "50d": "mist",
    "50n": "mist"
}

hava_durumu_tr = {
    "clear sky": "Acik hava",
    "few clouds": "Az bulutlu",
    "scattered clouds": "Parcali bulutlu",
    "broken clouds": "Cok bulutlu",
    "overcast clouds": "Kapali",
    "shower rain": "Saganak yagmur",
    "rain": "Yagmurlu",
    "light rain": "Hafif yagmurlu",
    "moderate rain": "Orta siddette yagmur",
    "heavy intensity rain": "Siddetli yagmur",
    "thunderstorm": "Gok gurultulu firtina",
    "thunderstorm with light rain": "Hafif yagmurlu firtina",
    "thunderstorm with rain": "Yagmurlu firtina",
    "snow": "Kar yagisli",
    "light snow": "Hafif kar yagisli",
    "heavy snow": "Yogun kar yagisli",
    "mist": "Sisli",
    "fog": "Yogun sis",
    "haze": "Puslu",
    "dust": "Tozlu",
    "sand": "Kumlu",
    "smoke": "Dumanli",
    "tornado": "Hortum",
    "squalls": "Bora"
}

def render(veri):
    ikon_kodu = veri["weather"][0]["icon"]
    meteocons_adi = ikon_eslesme.get(ikon_kodu, "not-available")
    image_address = f"https://cdn.meteocons.com/3.0.0-next.10/svg/fill/{meteocons_adi}.svg"

    aciklama_en = veri["weather"][0]["description"]
    turkcesi = hava_durumu_tr.get(aciklama_en, aciklama_en)

    return render_template("index.html",sehir_adi=veri["name"], sicaklik=veri["main"]["temp"],hava_durumu=turkcesi, image=image_address)

folder = os.path.dirname(os.path.abspath(__file__))
image_folder = os.path.join(folder, "/images")

load_dotenv()
api_key = os.getenv("API_KEY")
app = Flask(__name__)

@app.route("/")
def anasayfa():
    return render_template("index.html")

@app.route("/ara", methods=["POST", "GET"])
def ara():
    sehir = request.form["sehir"]
    url = f"https://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}&units=metric"

    response = requests.get(url)
    veri = response.json()

    if veri.get("cod") != 200:
        return render_template("index.html", error="Lutfen gecerli bir sehir adi giriniz!")
    return render(veri)
'''
    ikon_kodu = veri["weather"][0]["icon"]
    meteocons_adi = ikon_eslesme.get(ikon_kodu, "not-available")
    image_address = f"https://cdn.meteocons.com/3.0.0-next.10/svg/fill/{meteocons_adi}.svg"

    aciklama_en = veri["weather"][0]["description"]
    turkcesi = hava_durumu_tr.get(aciklama_en, aciklama_en)

    return render_template("index.html",sehir_adi=veri["name"], sicaklik=veri["main"]["temp"],hava_durumu=turkcesi, image=image_address)
'''

@app.route("/konum")
def konum():
    lat = request.args.get("lat")
    lon = request.args.get("lon")

    print("LAT: ", lat)
    print("LON: " , lon)

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    veri = response.json()

    print("VERI: ", veri)

    if veri.get("cod") != 200:
        return render_template("index.html", error="Lutfen gecerli bir sehir adi giriniz!")
    return render(veri)
'''
    ikon_kodu = veri["weather"][0]["icon"]
    meteocons_adi = ikon_eslesme.get(ikon_kodu, "not-available")
    image_address = f"https://cdn.meteocons.com/3.0.0-next.10/svg/fill/{meteocons_adi}.svg"

    aciklama_en = veri["weather"][0]["description"]
    turkcesi = hava_durumu_tr.get(aciklama_en, aciklama_en)

    return render_template("index.html",sehir_adi=veri["name"], sicaklik=veri["main"]["temp"],hava_durumu=turkcesi, image=image_address)
'''
if __name__ == "__main__":
    app.run(debug=False)

#https://cdn.meteocons.com/3.0.0-next.10/svg/fill/clear-day.svg