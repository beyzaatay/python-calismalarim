sayilar=[1,6,99,65,3,56]

toplam=0
adet=(len(sayilar))

for sayi in sayilar:
    toplam+=sayi

ortalama=toplam/adet
print("Sayıların Ortalaması: ", ortalama)