def second_max_number_in_list(lst):
    lst.sort(reverse=True)
    return lst[1]


lst = list(map(int, input('\nВведите числа через пробел: ').split()))

print(f'Второе по величине число в вашем списке это '
      f'{second_max_number_in_list(lst)}')
