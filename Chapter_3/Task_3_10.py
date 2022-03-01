list1 = [num for num in range(0, 10, 2)]
list2 = [num for num in range(1, 10, 2)]
list3 = []

for i in range(len(list1)):
    list3.append(list1[i])
    list3.append(list2[i])

print(f'\nlist1: {list1}\nlist2: {list2}')
print(f'list3: {list3}')
