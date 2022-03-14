from random import randint


def get_max_value(f: callable, x1: int, x2: int) -> int:
    """Возвращает максимальное значение (в целочисленных точка диапазона от x1
    до x1) из функции, переданной в качестве аргумента.

    :param f: функция с целочисленными значениями
    :type f: function
    :param x1: первая граница
    :type x1: int
    :param x2: вторая граница
    :type x2: int

    :rtype: int
    :return: максимальное значение из функции-аргумента
    """
    return max(f(x1, x2))


def get_random_values_in_list(x1: int, x2: int) -> list[int]:
    """Возвращает список со случайными значениями в диапазоне от x1 до x2.

    :param x1: первая граница
    :type x1: int
    :param x2: вторая граница
    :type x2: int

    :rtype: list[int]
    :return: список со случайными значениями в диапазоне от x1 до x2
    """
    lst = []
    for i in range(10):
        lst.append(randint(x1, x2))
    return lst


border1 = 1
border2 = 9

randomValues = get_random_values_in_list

print(f'\nСлучайные значения в функции: {randomValues(border1, border2)}')
print(f'Наибольшее значение в границах [{border1}, {border2}] равно '
      f'{get_max_value(randomValues, border1, border2)}')
