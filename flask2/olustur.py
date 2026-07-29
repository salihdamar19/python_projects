import pandas as pd
import os

klasor = os.path.dirname(os.path.abspath(__file__))
dosya = os.path.join(klasor, "durum.xlsx")

veri = {
    "Gorev" : ["Temizlik"],
    "Durum" : ["Yapilmadi"]
}

df = pd.DataFrame(veri)
df.to_excel(dosya, index=False)
print("Dosya olusturuldu!")