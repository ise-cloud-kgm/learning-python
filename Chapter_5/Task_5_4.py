text = input('\nВведите текст: ')

symbols = list(text)
newText = ''

for k in range(2, len(symbols), 3):
    newText += symbols[k] + symbols[k - 1] + symbols[k - 2]

print(f'Текст после замены: {newText}')
