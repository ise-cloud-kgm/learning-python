from random import randint


def maxvalue_and_index_in_list(lst):
    maxValue = max(lst)
    indexValue = lst.index(maxValue)
    return [maxValue, indexValue]


numbers = [randint(1, 9) for k in range(10)]

print(f'\nnumbers = {numbers}')
print(f'Максимальное значение, индекс = {maxvalue_and_index_in_list(numbers)}')
