number = int(input('\nВведите целое число: '))
print(f'Число битов равно {number.bit_length()}.')

bit = int(input('Введите номер бита: '))
print(f'Номер выбранного вами бита равен {(number>>bit) % 2}.')
