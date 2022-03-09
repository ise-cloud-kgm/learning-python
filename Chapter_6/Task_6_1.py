def compute_amount(numbers1: list, numbers2: list) -> int:
    """Вычислить сумму произведений попарных элементов двух списков.

    :param numbers1: первый список для вычисления суммы
    :type numbers1: list[int]
    :param numbers2: второй список для вычисления суммы
    :type numbers2: list[int]

    :rtype: int
    :return: сумма произведений попарных элементов
    """

    amount = 0

    size1, size2 = len(numbers1), len(numbers2)

    if size1 > size2:
        for k in range(size1):
            if k >= size2:  # если индекс больше длины второго списка
                j = 0
                # Циклично повторяем элементы второго списка.
                amount += numbers1[k] * numbers2[j]
                j += 1
            else:
                amount += numbers1[k] * numbers2[k]

    elif size1 < size2:
        for k in range(size2):
            if k >= size1:
                j = 0
                # Циклично повторяем элементы первого списка.
                amount += numbers1[j] * numbers2[k]
                j += 1
            else:
                amount += numbers1[k] * numbers2[k]

    else:
        for k in range(size1):
            amount += numbers1[k] * numbers2[k]

    return amount


nums1 = [num for num in range(6) if num % 2 == 0]
nums2 = [num for num in range(8) if num % 2 == 1]

print(f'\nСумма произведений попарных элементов списков равна '
      f'{compute_amount(nums1, nums2)}')
