def filling_snake(n):
    a = [[0] * n for i in range(n)]  # создание и заполнение матрицы нулями

    count = 0  # количество заполненных ячеек
    for i in range(n):  # заполнение 1 строки
        count += 1
        a[0][i] = count
    j = 0  # указываем последнюю заполненную ячейку
    i = n - 1
    n -= 1  # устанавливаем размер 1 блока 1 витка
    while len(a) ** 2 != count:  # условие выхода из цикла
        for k in range(n):  # движение вниз
            j += 1
            count += 1
            a[j][i] = count  # заполнение матрицы
        for k in range(n):  # движение влево
            i -= 1
            count += 1
            a[j][i] = count
        for k in range(n - 1):  # движение вверх
            j -= 1
            count += 1
            a[j][i] = count
        for k in range(n - 1):  # движение вправо
            i += 1
            count += 1
            a[j][i] = count
        n -= 2  # обеспечиваем переход на внутренний виток

    for i in range(len(a)):  # вывод полученной матрицы
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()


N = int(input('\nВведите размерность (N) матрицы NxN: '))

print('Двумерный список, заполненный змейкой (по спирали):')
filling_snake(N)
