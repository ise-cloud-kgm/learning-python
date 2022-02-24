firstNumber = int(input('\nВведите первое число: '))
secondNumber = int(input('Введите второе число: '))
thirdNumber = int(input('Введите третье число: '))

diff1 = secondNumber - firstNumber  # разница между вторым и первым числом
diff2 = thirdNumber - secondNumber  # разница между третьим и вторым числом

if diff1 == diff2:
    print('Введённые вами числа являются членами арифметической прогрессии')
else:
    print('Введённые вами числа не являются членами арифметической прогрессии')
