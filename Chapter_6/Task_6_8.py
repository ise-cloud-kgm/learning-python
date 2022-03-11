def compute_sum_of_geometric_progression(b1: int, q: int, n: int) -> int:
    """Рекурсивно вычисляет сумму геометрической прогрессии, учитывая, что
    первый её член равен единице.

    :param b1: первый член прогрессии, равный единице
    :type b1: int
    :param q: знаменатель геометрической прогрессии
    :type q: int
    :param n: количество членов прогрессии
    :type n: int

    :rtype: int
    :return: сумма геометрической прогрессии
    """
    if n == 0:
        return 0
    else:
        return b1 + compute_sum_of_geometric_progression(b1 * q, q, n - 1)


B1 = 1
Q = 2
N = 5

print(f'\nСумма геометрической прогрессии, состоящей из {N} членов '
      f'и имеющей знаменатель {Q}, равна '
      f'{compute_sum_of_geometric_progression(B1, Q, N)}')
