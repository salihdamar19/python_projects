def harf_notu_belirle(_not):
    if _not >= 90:
        return "AA"
    elif _not >= 80:
        return "BA"
    elif _not >= 70:
        return "CB"
    elif _not < 70:
        return "FF"

def ort_not_hesapla(dizi):
    ort_not = 0
    for _not in dizi:
        ort_not += _not/len(dizi)
    return ort_not

student = {
    "isim" : "Salih",
    "yas" : 21
}

student["notlar"] = [100,100,100,100,100]
student["not_ort"] = ort_not_hesapla(student["notlar"])
student["harf_notu"] = harf_notu_belirle(student["not_ort"])

print(f"Isim: {student["isim"]}")
print(f"Yas: {student["yas"]}")
print(f"Notlar: {student["notlar"]}")
print(f"Not ortalamasi: {student["not_ort"]}")
print(f"Harf notu: {student["harf_notu"]}")