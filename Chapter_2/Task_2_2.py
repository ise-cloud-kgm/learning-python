number = int(input('\nВведите целое число: '))

digitsOfNumbers = list(str(number))

index = 0

for i in digitsOfNumbers:
    digitsOfNumbers.pop(index)

    if int(i) == 0:
        digitsOfNumbers.insert(index, 9)

    elif int(i) == 1:
        digitsOfNumbers.insert(index, 8)

    elif int(i) == 2:
        digitsOfNumbers.insert(index, 7)

    elif int(i) == 3:
        digitsOfNumbers.insert(index, 6)

    elif int(i) == 4:
        digitsOfNumbers.insert(index, 5)

    elif int(i) == 5:
        digitsOfNumbers.insert(index, 4)

    elif int(i) == 6:
        digitsOfNumbers.insert(index, 3)

    elif int(i) == 7:
        digitsOfNumbers.insert(index, 2)

    elif int(i) == 8:
        digitsOfNumbers.insert(index, 1)

    elif int(i) == 9:
        digitsOfNumbers.insert(index, 0)

    index += 1

print('Число с заменами  - ', "".join(map(str, digitsOfNumbers)))
