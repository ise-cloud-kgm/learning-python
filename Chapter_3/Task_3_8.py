from random import randint

numbers = [randint(1, 20) for number in range(7)]

evenIndexes = []
oddIndexes = []

for index in range(len(numbers)):
    if index % 2 == 0:
        evenIndexes.append(numbers[index])
    else:
        oddIndexes.append(numbers[index])

evenIndexes.sort()
oddIndexes.sort(reverse=True)

newNumbers = []

for index in range(len(evenIndexes)):
    if index == len(evenIndexes) - 1 and len(evenIndexes) > len(oddIndexes):
        newNumbers.append(evenIndexes[index])
    else:
        newNumbers.append(evenIndexes[index])
        newNumbers.append(oddIndexes[index])


print(f'\nИзначальный список: {numbers}\n')
print(evenIndexes)
print(oddIndexes)
print(f'\nСписок после сортировки: {newNumbers}')
