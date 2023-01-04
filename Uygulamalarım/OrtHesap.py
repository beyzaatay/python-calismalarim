"notların ortalamasına göre kaldı mı geçti mi"

not1=float(input("İlk sınav:"))
not2=float(input("Son sınav:"))
ortalama=(not1+not2)/2
print("Ortalamanız:",ortalama)
if(ortalama<50):
    print("Kaldınız :(")
else:
    print("Tebrikler. Geçtiniz.")
