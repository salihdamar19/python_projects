#Olusturulacak text dosyasini projenin bulundugu klasorde olusturulmasi icin projenin tam konumunu aliyoruz

import os
klasor = os.path.dirname(os.path.abspath(__file__))
dosya_yolu = os.path.join(klasor, "notlar.txt")


# Dosyaya yazma
with open(dosya_yolu, "w") as f:
    f.write("Salih\nDamar\nCok iyi bir muhendis olacak")

#Tum dosyayi okuma
with open(dosya_yolu, "r") as f:
    print(f.read())

# Dosyadan satir satir okuma
with open(dosya_yolu, "r") as f:
    for satir in f:
        print(satir.strip())