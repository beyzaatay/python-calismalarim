name = 'Beyza Atay'

for letter in name:
    if letter == 'y':
        continue
    print(letter)

x = 0

while x < 5:
    if x == 2:
        break
    x += 1
    print(f'while döngüsü break {x}')

while x < 5:
    x += 1
    if x == 2:
        continue

    print(f'while döngüsü continue {x}')



a = 0
toplam = 0
while a <= 100:
    a += 1
    if a % 2 == 0:
        continue
    toplam += a

print(f'toplam {toplam}')