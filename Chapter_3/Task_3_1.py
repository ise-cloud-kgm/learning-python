text = input('\nВведите текст: ')
indexIncrement = int(input('Введите приращение по индексу: '))

tuple1 = tuple(text)
tuple2 = tuple1[::indexIncrement]

print(f'\nПервый кортеж: {tuple1}\nВторой кортеж: {tuple2}')
