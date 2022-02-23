# Функция для вычисления факториала.
def compute_factorial(n):
    fact = 1

    for k in range(1, n + 1):
        fact *= k

    return fact


n = int(input('\nВведите число, факториал которого необходимо вычислить: '))

while n < 0:
    print(f'\nЧисло {n} < 0, что не соответствует условию задачи.')
    n = int(input('Введите число заново: '))

print(f'{n}! = {compute_factorial(n)}')
