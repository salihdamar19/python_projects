#Simple to do List
#Author: Salih Damar

import os
klasor = os.path.dirname(os.path.abspath(__file__))
dosya_yolu = os.path.join(klasor, "gorevler.txt")


def kullanici_secim():
    try:
        global secim
        secim = str(input('ekle/tamamla/listele/cikis\nSeciminiz: '))
    except ValueError:
        print('Lutfen metin turunde girdi yaziniz!')
    if secim == 'ekle' or secim == 'tamamla' or secim == 'listele' or secim == 'cikis':
         return secim
    else:
        print('Lutfen gecerli bir secim yapiniz!')

def baslik_al():
    try:
        baslik = str(input('Gorev basligini giriniz: '))
    except ValueError:
        print('Lutfen basligi metin turunde giriniz!')
    else:
        print('Baslik basariyla tanimlandi.')
        return baslik
    finally:
        print('Islem sonlandirildi.')

def dosya_yaz(baslik):
    with open('gorevler.txt', 'a+') as f:
        f.write(f"[ ]|{baslik}\n")
        print('Baslik basariyla eklendi.')

#.split kullanilacak
def dosya_gorev_tamamla(gorev):
    dosya_icerigi = []
    with open('gorevler.txt', 'r') as f:
        for satir in f:
            eleman = satir.strip().split('|')
            if eleman[1] == gorev:
                eleman[0] = "[X]"
                dosya_icerigi.append(f"{eleman[0]}|{eleman[1]}\n")
            else:
                dosya_icerigi.append(satir.strip())
    with open('gorevler.txt', 'w') as f:
        for satir in dosya_icerigi:
            f.write(satir.strip())


def dosya_oku():
    with open('gorevler.txt', 'r') as f:
        print('[ ]/[X]: Gorev Durumu\n************************')
        for satir in f:
            print(f"{satir.strip().split('|')[0]} {satir.strip().split('|')[1]}")


kullanici_secim()
while secim != 'cikis':
    if secim == 'ekle':
        baslik = baslik_al()
        dosya_yaz(baslik)
    elif secim == 'tamamla':
        baslik = baslik_al()
        dosya_gorev_tamamla(baslik)
    elif secim == 'listele':
        dosya_oku()
    kullanici_secim()
