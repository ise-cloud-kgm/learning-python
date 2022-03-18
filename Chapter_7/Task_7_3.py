number = int(input('\nВведите целое число: '))

count = 0
for bit in str(bin(number))[2:]:
    count += int(bit)

print(f'\nВсе биты числа {number}: {str(bin(number))[2:]}')
print(f'Сумма всех битов в десятичном представлении: {count}')

print(f'\nСумма всех битов в бинарном представлении: {str(bin(count))[2:]}')
