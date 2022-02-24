try:
    number1 = float(input('\nВведите первое число: '))
except ValueError:
    print(f'Введённое значение не является числом')

try:
    number2 = float(input('Введите второе число: '))
except ValueError:
    print(f'Введённое значение не является числом')

print(f'{number1} > {number2}') if number1 > number2 else \
print(f'{number1} < {number2}')
