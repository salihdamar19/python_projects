from flask import Flask, render_template, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)
klasor = os.path.dirname(os.path.abspath(__file__))
dosya = os.path.join(klasor, "durum.xlsx")
durum = "white"

@app.route("/")
def sayfa():
    df = pd.read_excel(dosya)
    return render_template("index.html", df=df)

@app.route("/degistir/<gorev_adi>")
def degistir(gorev_adi):
    df = pd.read_excel(dosya)
    g_index = df[df["Gorev"] == gorev_adi].index[0]
    yeni_deger = "Yapildi" if df.loc[g_index, "Durum"] == "Yapilmadi" else "Yapilmadi"
    df.loc[g_index, "Durum"] = yeni_deger
    df.to_excel(dosya, index=False)
    #global durum
    #durum = "green" if durum == "white" else "white"
    return redirect(url_for("sayfa"))


if __name__ == "__main__":
    app.run(debug=True)