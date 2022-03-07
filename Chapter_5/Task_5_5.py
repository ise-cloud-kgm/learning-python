text1 = input('\nВведите первую строку: ')
text2 = input('Введите вторую строку: ')
text3 = ''

size1 = len(text1)
size2 = len(text2)

if size1 > size2:
    for i in range(size1):
        if i > size2 - 1:
            text3 += text1[i] + '*'
        else:
            text3 += text1[i] + text2[i]
elif size1 < size2:
    for i in range(size2):
        if i > size1 - 1:
            text3 += text2[i] + '*'
        else:
            text3 += text1[i] + text2[i]
elif size1 == size2:
    for i in range(size2):
        text3 += text1[i] + text2[i]

print(f'Третья строка: {text3}')
