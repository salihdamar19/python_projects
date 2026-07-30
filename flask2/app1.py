from flask import Flask, render_template, redirect, url_for
import pandas as pd
import os

klasor = os.path.dirname(os.path.abspath(__file__))
dosya = os.path.join(klasor, "Hatim_Takip.xlsx")

app = Flask(__name__)


@app.route("/")
def sayfa():
    df = pd.DataFrame(dosya)
    aylar = df.
    return render_template("index2.html", aylar = aylar)

@app.route("/degistir", methods = ["POST"])

if __name__ == "__main__":
    app.run(debug=True)