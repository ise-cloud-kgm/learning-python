number = int(input('\nВведите целое число: '))

for i in range(10):
    sumOfDigits = 0

    if str(i) not in str(number):
        print(f'В числе {number} нет вхождений цифры {i}')
    else:
        for k in str(number):
            if k == str(i):
                sumOfDigits += 1
        print(f'В числе {number} находится {sumOfDigits} вхождений цифры {i}')
