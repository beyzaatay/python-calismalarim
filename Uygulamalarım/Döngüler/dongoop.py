for item in range(10, 100, 20):
    print(item)

print(list(range(10, 100, 5)))

greeting = 'Hello'

for item in enumerate(greeting):
    print(item)



list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = [100, 200, 300, 400, 500]



for item in list(zip(list1, list2, list3)):
    print(item)

for a, b, c in list(zip(list1, list2, list3)):
    print(a, b)