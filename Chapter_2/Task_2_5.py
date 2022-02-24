values = [int(i) for i in input('\nВведите значения через пробел: ').split()]
upperBound = int(input('Введите верхнюю границу: '))

count = 0

for i in range(1, upperBound + 1):
    if i in values:
        continue
    count += i

print(f'Сумма натуральных чисел от 1 до {upperBound} '
      f'(без учёта введённых вами чисел) равна {count}')
