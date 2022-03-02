from random import randint

numbers = []

for i in range(15):
    if i < 5:
        numbers.append(randint(1, 10))
    else:
        numbers.append(randint(10, 30))

print(f'\nnumbers: {numbers}')
