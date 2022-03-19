def stars(some_description: callable):
    """Оборачиваем функцию с описанием задачи символами '*'."""
    def wrapper():
        print(f'\n\t', '*' * 3, end=' ')
        some_description()
        print('*' * 3, '\n')

    return wrapper


@stars
def description():
    print('Комплексные числа вводятся в формате "1+2j", "3-5j", "4", "5j" и '
          'т.д.', end=' ')


def sum_two_complex(first_complex: complex, second_complex: complex):
    return first_complex + second_complex


def difference_two_complex(first_complex: complex, second_complex: complex):
    return first_complex - second_complex


def multiply_two_complex(first_complex: complex, second_complex: complex):
    return first_complex * second_complex


def division_two_complex(first_complex: complex, second_complex: complex):
    return first_complex / second_complex


description()

while True:
    try:
        complex1 = complex(input('Введите первое комплексное число: '))
        complex2 = complex(input('Введите второе комплексное число: '))
        break
    except ValueError:
        print(f'\n\tВведено не комплексное число!\n')

amount = sum_two_complex(complex1, complex2)
difference = difference_two_complex(complex1, complex2)
products = multiply_two_complex(complex1, complex2)
quotient = division_two_complex(complex1, complex2)
absComplex1 = abs(complex1)
absComplex2 = abs(complex2)

print(f'\nСумма комплексных чисел: {amount}')
print(f'Разница комплексных чисел: {difference}')
print(f'Произведение комплексных чисел: {products}')
print(f'Частное комплексных чисел: {quotient}')

if absComplex1 > absComplex2:
    print(f'|{complex1}| = {absComplex1}  >  {absComplex2} = |{complex2}|')
elif absComplex2 > absComplex1:
    print(f'|{complex2}| = {absComplex2}  >  {absComplex1} = |{complex1}|')
else:
    print(f'|{complex2}| = {absComplex2}  =  {absComplex1} = |{complex1}|')
