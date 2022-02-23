def fibonacci(n):
    current = 1
    if n > 2:
        current = fibonacci(n - 1) + fibonacci(n - 2)
    return current

number = int(input('\nВведите количество чисел Фибоначчи: '))

for count in range(number):
    print(fibonacci(count), end=' ')
