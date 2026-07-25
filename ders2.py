def sehirleri_yazdir():
    for i, sehir in enumerate(sehirler, start=1):
        print(f"{i}. {sehir}")

sehirler = ['istanbul', 'bursa', 'ankara', 'nigde', 'canakkale']

sehirleri_yazdir()

sehirler.append('izmir')

print("Listenin yeni hali:")
sehirleri_yazdir()
