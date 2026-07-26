#author: salih damar
try:
    sayi1 = int(input('Lutfen birinci sayiyi giriniz: '))
    sayi2 = int(input('Lutfen ikinci sayiyi giriniz: '))
    sonuc = sayi1/sayi2
except ValueError:
    print('Lutfen gecerli bir sayi giriniz!')
except ZeroDivisionError:
    print('Sifira bolunme islemi yapilamadi!')
    
#bunlarin yerine 
#   exceppt (ValueError, ZeroDivisionError) as e:
#       print(f"bir hata olustu: {e}")
# kullanailabilir            

else:
    print(f"{sayi1}/{sayi2} = {sonuc}")
finally:
    print('Islem sonlandirildi.')