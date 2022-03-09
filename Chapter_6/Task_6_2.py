def get_odd_list(numbers: list[int]) -> list[int]:
    """Возвращает список, в который включены
    только нечетные числа из списка-аргумента.

    :param numbers: список, из которого отбираются нечётные значения
    :type numbers: list[int]

    :rtype: list[int]
    :return: список с нечётными числами из списка-аргумента
    """
    odd_numbers = []

    for number in numbers:
        if number % 2 == 1:
            odd_numbers.append(number)

    return odd_numbers


nums = list(range(10))

print(f'\nСписок = {nums}')
print(f'Нечётные числа из этого списка: {get_odd_list(nums)}')
