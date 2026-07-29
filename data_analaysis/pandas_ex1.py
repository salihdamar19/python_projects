import pandas as pd
import os

klasor = os.path.dirname(os.path.abspath(__file__))
dosya = os.path.join(klasor, "basarili_ogrenciler.csv")

ogrenciler = {
    "isim" : ["Salih", "Greenwood", "Vedat", "Asensio", "Fred"],
    "not1" : [100, 100, 100, 100, 0],
    "not2" : [100, 100, 100, 100, 0],
    "not3" : [100, 99, 80, 1, 0]
}

df = pd.DataFrame(ogrenciler)
df["ortalama"] = (df["not1"] + df["not2"] + df["not3"]) / 3

basarili_ogrenciler = df[df["ortalama"] > 70].sort_values("ortalama", ascending=False)
#print(basarili_ogrenciler)
basarili_ogrenciler.to_csv(dosya, index=False)