#Author: Salih Damar
#Olusturulacak text dosyasini projenin bulundugu klasorde olusturulmasi icin projenin tam konumunu aliyoruz

import os
klasor = os.path.dirname(os.path.abspath(__file__))
dosya_yolu = os.path.join(klasor, "notlar.txt")


# Dosyaya yazma
with open(dosya_yolu, "w") as f:
    f.write("Salih Damar: 100\nVedat Muriqi: 100\nMason Greenwood: 100\n")

#Tum dosyayi okuma
with open(dosya_yolu, "r") as f:
    print(f.read())

# Dosyadan satir satir okuma
with open(dosya_yolu, "r") as f:
    for satir in f:
        print(satir.strip())

#Claude'in verdigi gorev
with open(dosya_yolu, "r") as f:
    icerik = ""
    for i, satir in enumerate(f, start=1):
        icerik += f"{i}. {satir}"
    print(f"\n{icerik}")

#Olmayan dosyayi okumaya calisma
try:
    with open("veri.txt", "r") as f:
        icerik = f.read()
except FileNotFoundError:
    print('Dosya bulunamadi!')
else:
    print(icerik)