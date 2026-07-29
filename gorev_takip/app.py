from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)
klasor = os.path.dirname(os.path.abspath(__file__))
dosya = os.path.join(klasor, "Hatim_Takip.xlsx")

@app.route("/")
def sayfa():
    df = pd.read_excel(dosya)
    df = df.fillna("Okunmadı")   # NaN olan hucreleri "Yapilmadi" say
    aylar = df.columns[1:]        # ilk sutun (Ad Soyad) haric hepsi ay
    return render_template("index.html", df=df, aylar=aylar)

@app.route("/degistir", methods=["POST"])
def degistir():
    isim = request.form["isim"]
    ay = request.form["ay"]

    df = pd.read_excel(dosya)
    df = df.fillna("Okunmadı")

    satir_index = df[df["Ad Soyad"] == isim].index[0]
    mevcut_deger = df.loc[satir_index, ay]

    yeni_deger = "Okunmadı" if mevcut_deger == "Okundu" else "Okundu"
    df.loc[satir_index, ay] = yeni_deger

    df.to_excel(dosya, index=False)
    return redirect(url_for("sayfa"))

if __name__ == "__main__":
    app.run(debug=True)