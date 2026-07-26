#bunun algoritmasini kurmak gercekten ugrastirdi gecenin dordu diye midir bilmiyorum
def dizi_yazdir(liste):
    for eleman in liste:
        print(eleman)

def iki_kat(sayi):
    return sayi*2

sayilar = [1,2,3,4,5]
iki_kat_sayilar = []

for sayi in sayilar:
    iki_kat_sayilar.append(iki_kat(sayi))

print("Sayilar dizisi: ")
dizi_yazdir(sayilar)
print("iki kat sayilar dizisi: ")
dizi_yazdir(iki_kat_sayilar)
