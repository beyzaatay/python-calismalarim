def ehliyet():
    name = input('İsminiz : ').upper()
    age = int(input('Yaşınız : '))
    edu_status = input('Eğitim durumunuz : ').lower()


    if (age >= 18) :
        if(edu_status == 'lise' or (edu_status == 'üniversite' or edu_status == 'lisans')):
            print(f'{name} ehliyet alamaya uygun. Yaş : {age} Eğitim durumu : {edu_status.upper()}')
        else:
            print(f'{name} öğrenim durumunuz "{edu_status.upper()}" ehliyet almaya uygun değil')
    else:
        print(f'{name} yaşınız "{age}" ehliyet alamaya uygun değil.')