number = int(input('\nВведите целое число: '))

digits = []

for digit in str(number):
    digits.append(int(digit))

print(f'Кортеж в прямом порядке: {digits}')
print(f'Кортеж в обратном порядке: {digits[::-1]}')
