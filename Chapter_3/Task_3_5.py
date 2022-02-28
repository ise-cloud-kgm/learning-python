from random import randint

n = 5  # количество строк
m = 5  # количество столбцов

# Создание и заполнение двумерного списка случайными буквами лат. алфавита.
matrix = [[chr(randint(97, 122)) for i in range(n)] for j in range(m)]

print(f'\nДвумерный список {n}x{m} до удаления:')
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()

rowToDelete = int(input('\nВведите строку для удаления: '))
colToDelete = int(input('Введите столбец для удаления: '))

del matrix[rowToDelete - 1]  # удаление строки
for row in matrix:
    del row[colToDelete - 1]  # удаление столбца

print(f'\nДвумерный список {n - 1}x{m - 1} после удаления:')
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()
