from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)
klasor = os.path.dirname(os.path.abspath(__file__))
dosya = os.path.join(klasor, "durum.xlsx")
durum = "white"

@app.route("/")
def sayfa():
    df = pd.read_excel(dosya)
    gorev_durumu = df.loc[0, "Durum"]
    return render_template("index.html", durum=gorev_durumu)

@app.route("/degistir")
def degistir():
    df = pd.read_excel(dosya)
    mevcut = df.loc[0, "Durum"]
    yeni_deger = "Yapildi" if mevcut == "Yapilmadi" else "Yapilmadi"
    df.loc[0, "Durum"] = yeni_deger
    df.to_excel(dosya, index=False)
    #global durum
    #durum = "green" if durum == "white" else "white"
    return sayfa()


if __name__ == "__main__":
    app.run(debug=True)