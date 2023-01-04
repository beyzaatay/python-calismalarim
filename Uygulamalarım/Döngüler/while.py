x = 0

while x < 100:
    print(x)
    x += 1
print("while döngüsü bitti")



y = 0
while y < 100:
    if (y % 2 == 0):
        print(f'çift sayılar : {y}')
    y += 1




name = ""

while not name:
    name = input("İsminiz :")
    if name == '':
        print('İsim girmeniz zorunludur')
print(f'Merhaba {name}')