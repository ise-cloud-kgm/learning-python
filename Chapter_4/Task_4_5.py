size = 7

list1 = [k * 2 + 1 for k in range(size)]
list2 = [k * 2 + 1 for k in range(1, size + 1)]

setOfTuples = set()

for k, j in zip(list1, list2):
    setOfTuples.add((k, j))

print(f'\nМножество кортежей: {setOfTuples}')
