def print_values(fn: callable) -> callable:
    """Выводит введённые элементы, а также среднее, максимальное и
    минимальные значения на основе введённых элементов.

    :param fn: функция, которой мы дополняем функционал для вывода элементов
    :type fn: function

    :rtype: function
    :return: вывод элементов списка, среднее, макс. и мин. значения
    """

    def wrapper(*args):
        print('\nЭлементы списка:', *args)
        print(f'Среднее, максимальное и минимальное значения: {fn(*args)}')

    return wrapper


@print_values
def get_list_average_min_max_values(*numbers: tuple[float]) -> list[float]:
    """Вычисляет среднее, максимальное и среднее значения и возвращает
    результат в виде списка из трёх элементов.
    """
    return [round(sum(numbers) / len(numbers), 2), max(numbers), min(numbers)]


get_list_average_min_max_values(1, 312, -1, 3.2, 4, 2, 54, 2, 0)
