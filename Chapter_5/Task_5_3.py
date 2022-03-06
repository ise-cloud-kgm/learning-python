text = input('\nВведите текст: ')

newText = ''
for symbol in text:
    if symbol.isupper():
        newText += symbol.lower()
    else:
        newText += symbol.upper()

print(f'Текст после преобразований: {newText}')
