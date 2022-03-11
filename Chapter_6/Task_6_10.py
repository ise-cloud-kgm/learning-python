def compute_degrees_of_two(quantity_of_elements: int) -> iter:
    """Перебивает степени двойки.

    :param quantity_of_elements: количество степеней двойки
    :type quantity_of_elements: int

    :rtype: iter
    :return: степень двойки
    """
    for number in range(0, quantity_of_elements):
        yield 2**number


quantityOfElements = 8
degreesOfTwo = compute_degrees_of_two(quantityOfElements)

print(f'\n{quantityOfElements} степеней двойки:')
for index, number in enumerate(degreesOfTwo):
    print(f'{index + 1} число - {number} ')
