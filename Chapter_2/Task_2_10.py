try:
    a = float(input('\nВведите параметр A: '))
    b = float(input('Введите параметр B: '))

    if a != 0:
        x = (b - 1) / a - 1
        print(f'Решение уравнение: x = {x}')
    elif a == 0 and b == 1:
        print('Решением уравнения является любое число')
    elif a == 0 and b != 1:
        print('Уравнение не имеет решений')

except (TypeError, ValueError):
    print('Ошибка! Вы неправильно ввели одно или два числа!')
