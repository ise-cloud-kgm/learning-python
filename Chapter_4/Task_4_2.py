number1 = int(input('\nВведите первое число: '))
number2 = int(input('Введите второе число: '))

setDigits1 = set(str(number1))
setDigits2 = set(str(number2))

generalDigits = setDigits1.intersection(setDigits2)

print(f'Цифры, которые есть в представлении обоих чисел: {generalDigits}')
