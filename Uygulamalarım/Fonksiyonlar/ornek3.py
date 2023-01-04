def tamBolenleriBul(sayi):
    tamBolenler = []
    for i in range(1, sayi):
        if sayi % i == 0:
            tamBolenler.append(i)

    return tamBolenler


print(tamBolenleriBul(25))