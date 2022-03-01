from random import randint

numbers = [randint(1, 9) for num in range(4)]

print(f'\nСписок до добавления элементов: {numbers}')

insertedNumbers = []  # Список с числами, которые вставляются между элементами.

for i in range(len(numbers)):
    if i == len(numbers) - 1:
        break
    insertedNumbers.append(numbers[i] + numbers[i + 1])

j = 0
for index in range(1, len(insertedNumbers) * 2, 2):
    numbers.insert(index, insertedNumbers[j])
    j += 1

print(f'Список после добавления элементов: {numbers}')
