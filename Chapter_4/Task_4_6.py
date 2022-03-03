number = int(input('\nВведите число (>= 1): '))

while number < 1:
    print(f'\nВведённое вами число не соответствует условию.')
    number = int(input('Введите число (>= 1) заново: '))

numbers = []
for num in range(1, number + 1):
    numbers.append(num)

dictNumbers = {num:numbers[-num] for num in numbers}

print(f'\nСловарь: {dictNumbers}')

