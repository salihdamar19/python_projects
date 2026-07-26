class Hesap:
    def __init__(self, isim):
        self.sahibi = isim
        self.bakiye = 0

    def yatir(self, miktar):
        self.bakiye += miktar
        print(f'Para yatirma islemi gerceklestirildi.\nGuncel Bakiye: {self.bakiye}\n')
    def cek(self, miktar):
        if miktar > self.bakiye:
            print('Yetersiz Bakiye!\n')
        else:
            self.bakiye -= miktar
            print(f'Para cekme islemi gerceklestirildi.\nGuncel Bakiye: {self.bakiye}\n')

    def bakiye_goster(self):
        print(f"Guncel Bakiye: {self.bakiye}\n")

h1 = Hesap("Salih")
h1.yatir(500)
h1.cek(200)