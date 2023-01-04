def Arttir(x):
    return x*1,5
kisi=["Beyza","Ali","Damla","Kemal"]
maas=[2000,1500,3000,4000]
yeniMaas=list(map(Arttir,maas))
sonuc=list(zip(kisi,yeniMaas))

for i,k in sonuc:
    print("{} isimli kişinin zamlı maaşı : {}".format(i,k))