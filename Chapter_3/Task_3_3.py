from random import randint


def list_of_random_symbols(size1, size2):
    lst = [[chr(randint(97, 122)) for i in range(size1)] for j in range(size2)]
    return lst


row = 3
col = 3

print(f'\nДвумерный список размером {row}x{col} со случайными буквами: '
      f'{list_of_random_symbols(row, col)}')
