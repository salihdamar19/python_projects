import pandas as pd
import numpy as np
import os

klasor = os.path.dirname(os.path.abspath(__file__))
dosya = os.path.join(klasor, "tum_ogrenciler.csv")

def durum_belirleyici(ortalama):
    if ortalama >= 70:
        return "Gecti"
    else:
        return "Kaldi"

ogrenciler = {
    "isim" : ["Salih", "Greenwood", "Vedat", "Asensio", "Fred"],
    "not1" : [100, 100, 100, 100, 0],
    "not2" : [100, 100, 100, 100, 0],
    "not3" : [100, 100, 80, 1, 0]
}

df = pd.DataFrame(ogrenciler)
df["ortalama"] = (df["not1"] + df["not2"] + df["not3"]) / 3


print(f"Sinif Ortalamasi: {df["ortalama"].mean()}")
en_basarili_index = df["ortalama"].idxmax()
en_basarili = df.loc[en_basarili_index]
print(en_basarili["isim"], en_basarili["ortalama"])

df["durum"] = df["ortalama"].apply(durum_belirleyici)
#df["durum"] = np.where(df["ortalama"] >= 70, "Gecti", "Kaldi")

df.to_csv(dosya, index=False)

print(df)
