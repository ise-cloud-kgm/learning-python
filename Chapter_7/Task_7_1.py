base = input('\nВведите основание для системы счисления (2, 8 или 16): ')

# Проверка, ввёл ли пользователь корректное значение для основания.
while not (base == '2' or base == '8' or base == '16' or base.isdecimal()):
    print(f'\n\t*** Вы ввели основание, которое не соответствует значениям '
          f'(2, 8 или 16)! ***')
    base = input('\nВведите основание заново: ')

number = input('Введите число (в десятичной системе счисления): ')

# Проверка, ввёл ли пользователь корректное значение для десятичного числа.
while not number.isdecimal() or number[0] == '0':
    print(f'\n\t*** Вы ввели некорректное значение десятичного числа! ***')
    number = input('\nВведите число заново: ')

newNumber = ''

if base == '2':
    newNumber = str(bin(int(number)))[2:]  # Убираем префикс 0b.
    print(f'Результат перевода: {number}[{10}] = {newNumber}[{base}]')
elif base == '8':
    newNumber = str(oct(int(number)))[2:]  # Убираем префикс 0o.
    print(f'Результат перевода: {number}[{10}] = {newNumber}[{base}]')
elif base == '16':
    newNumber = str(hex(int(number)))[2:]  # Убираем префикс 0x.
    print(f'\nРезультат перевода: {number}[{10}] = {newNumber}[{base}]')
