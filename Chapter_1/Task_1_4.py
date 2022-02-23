listSize = int(input('Введите размер списка: '))

listOfPowerOfTwo = [2 * k for k in range(listSize)]

print(f'Список с размерностью [{listSize}], '
      f'содержащий степени двойки: {listOfPowerOfTwo}')
