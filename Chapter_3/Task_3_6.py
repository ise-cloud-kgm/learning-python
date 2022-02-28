numbers = [1, 0, 2, 3, 5, 4, 9, 6, 8, 7]

for i in range(len(numbers) - 1):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(f'\nnumbers = {numbers}')
