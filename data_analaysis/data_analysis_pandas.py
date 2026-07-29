import pandas as pd
import os

klasor = os.path.dirname(os.path.abspath(__file__))
dosya = os.path.join(klasor, "veri.csv")

veri = {
    "isim" : ["Ahmet", "Mehmet", "Ayse", "Fatma", "Hayriye"],
    "yas" : [24,21,35,49,55],
    "sehir" : ["Bursa", "Istanbul", "Izmir", "Canakkale", "Balikesir"]
}

df = pd.DataFrame(veri)
print(df)

df["yas"] # sadece bir sutunu sec
df[df["yas"] > 21] # filtreleme
df["yas"].mean() # sutun ortalamasi
df.sort_values("yas") # yasa gore siralama
df.to_csv(dosya, index=False)
df = pd.read_csv(dosya)
print(df.sort_values("yas"))