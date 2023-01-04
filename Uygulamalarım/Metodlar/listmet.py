from logging.config import valid_ident


numbers = [1,8,10,5,10,6,9]
letters = ['a','g','y','c','u','i']

val=min(numbers)
val=max(numbers)
val=max(letters)

numbers.append(49)

numbers.insert(3,79)
numbers.insert(-1,44)

numbers.pop(0)
numbers.remove(44)


letters.sort()

numbers.reverse()

print(numbers.count(10))

print(f'numbers: {numbers} \nletters: {letters}')