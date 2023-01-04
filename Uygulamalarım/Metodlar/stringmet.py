website="www.beyzaatay.com"
course= "Matematik Kursu: "


helloworld=' Hello World ' ; helloworld=helloworld.strip() ; print(helloworld)

ta='www.beyzaatay.com' ; ta=ta.lstrip('www.').rstrip('.com') ; print(ta)
ta='www.beyzaatay.com' ; ta=ta.strip('w.com') ; print(ta)

course=course.lower() ; print(course)

kactaneavar=website.count('a') ; print(kactaneavar)

kontrol=website.startswith('www'),website.endswith('.com') ; print(kontrol)

bul=website.find('.com') ; print(f'6- {bul}')

alfa=course.isalpha() ; print(alfa)

icerik='Contents' ; icerik=icerik.center(50,'*') ; print(icerik)

tire=course.replace(' ','-') ; print(tire)

ayir=course.split(' ') ; print(ayir)