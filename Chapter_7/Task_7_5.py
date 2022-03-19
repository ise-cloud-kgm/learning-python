from fractions import Fraction


def stars(some_description: callable):
    """Оборачиваем функцию с описанием задачи символами '*'."""
    def wrapper():
        print(f'\n\t', '*' * 3, end=' ')
        some_description()
        print('*' * 3, '\n')

    return wrapper


@stars
def description():
    print('Рациональные дроби вводятся в формате "1/5", "2/5" и т.д.', end=' ')


def sum_two_fractions(first_fraction: Fraction, second_fraction: Fraction):
    return first_fraction + second_fraction


def difference_two_fractions(first_fraction: Fraction,
                             second_fraction: Fraction):
    return first_fraction - second_fraction


def multiply_two_fractions(first_fraction: Fraction,
                           second_fraction: Fraction):
    return first_fraction * second_fraction


def division_two_fractions(first_fraction: Fraction,
                           second_fraction: Fraction):
    return first_fraction / second_fraction


description()

while True:
    try:
        fraction1 = Fraction(input('Введите первую рациональную дробь: '))
        fraction2 = Fraction(input('Введите вторую рациональную дробь: '))
        break
    except ValueError:
        print(f'\n\tВведён нечисловой тип данных!\n')
    except ZeroDivisionError:
        print(f'\n\tПопытка деления на ноль!\n')


amount = sum_two_fractions(fraction1, fraction2)
difference = difference_two_fractions(fraction1, fraction2)
products = multiply_two_fractions(fraction1, fraction2)
quotient = division_two_fractions(fraction1, fraction2)
maxValue = max(amount, difference, products, quotient)
minValue = min(amount, difference, products, quotient)


print(f'\nСумма дробей: {amount}')
print(f'Разница дробей: {difference}')
print(f'Произведение дробей: {products}')
print(f'Частное дробей: {quotient}')
print(f'Наибольшее среди полученных значений: {maxValue}')
print(f'Наименьшее среди полученных значений: {minValue}')
