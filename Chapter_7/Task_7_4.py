number = int(input('\nВведите целое число: '))

octNumber = str(oct(number))[2:]

print(f'{number}[10] = {octNumber}[8] = reversed {octNumber[::-1]}[8]')
