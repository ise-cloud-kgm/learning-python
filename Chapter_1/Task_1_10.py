def sum_of_odd_numbers(quantity_of_numbers):
    summa = 0

    for k in range(quantity_of_numbers):
        summa += 2 * k + 1

    return summa


quantityOfNumbers = int(input('\nВведите количество чисел: '))

print(f'Сумма {quantityOfNumbers} чисел равна '
      f'{sum_of_odd_numbers(quantityOfNumbers)}')
