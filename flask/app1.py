from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def anasayfa():
    isim = "Salih"
    yas = 22
    dersler = ["Python", "C++", "Matematik", "Fizik"]
    return render_template("index.html", kullanici_adi=isim, kullanici_yas=yas, ders_listesi = dersler)

@app.route("/merhaba", methods=["POST"])
def merhaba():
    isim = request.form["kullanici_isim"]
    return f"Merhaba {isim}, hos geldin!"
    #isim = request.args.get("kullanici_isim", "").strip()
    #if not isim:
        #return "Hata: Isim girmeden gonderemezsin!"
    

if __name__ == "__main__":
    app.run(debug=True)