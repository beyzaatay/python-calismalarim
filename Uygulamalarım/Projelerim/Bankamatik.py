print("""
**********************************



ATAY Bankasına Hoş Geldiniz

Lütfen Yapmak İstediğiniz işlemi Seçiniz.

Sistemden Çıkmak için  : "X" Tuşuna Basınız

Bakiye Sorgulamak için : 1

Para Yatırmak için     : 2

Para Çekmek için       : 3



**********************************
""")


bakiye = 1000

while True:

    işlem = input("Lütfen Yapmak istediğiniz işlemi Seçiniz\n")

    if (işlem == "X"):


        print("Bankamızı Tercih Ettiğiniz\n için Teşekür Ederiz. Yine Bekleriz.")

        break


    elif(işlem == "1"):

        print("Bakiyeniz {} TL'dir".format(bakiye))


    elif (işlem == "2"):

        yatırılan = int(input("Lütfen Yatırmak istediğiniz Parayı Rakamla Yazınız."))

        bakiye = bakiye + yatırılan

        print("Bakiyeniz {} TL'dir".format(bakiye))

    elif (işlem == "3"):

        cekilen = int(input("Lütfen Çekmek istediğiniz Parayı Rakamla Tuşlayınız."))



        if (bakiye - cekilen < 0):

            print("Böyle Bir Miktar Çekemezsiniz!")


        else:

            bakiye = bakiye - cekilen

            print("Bakiyeniz {} TL'dir.".format(bakiye))


    else:

        print("Yanlış Bir işlem Yaptınız.")
