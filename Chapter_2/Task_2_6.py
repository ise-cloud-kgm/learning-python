a = float(input('\na = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a:
    print(f'Треугольник со сторонами {a}, {b} и {c} существует')
else:
    print(f'Треугольник со сторонами {a}, {b} и {c} не существует')
