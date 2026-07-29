from flask import Flask

app = Flask(__name__)

@app.route("/")
def anasayfa():
    return "Merhaba Salih!"

@app.route("/hakkimda")
def hakkimda():
    return "Ben salih Bilgisayar Muhendisligi ogrencisiyim."

@app.route("/selamla/<isim>")
def selamla(isim):
    return f"Selam {isim}!"

@app.route("/kare/<int:sayi>")
def kare(sayi):
    return f"sayi : {sayi}<br> sayinin karesi : {sayi*sayi}"


if __name__ == "__main__":
    app.run(debug=True)