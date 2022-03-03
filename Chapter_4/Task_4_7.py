text = input('\nВведите текст: ')

dictText = {}
for symbol in text:
    dictText[symbol] = text.count(symbol)

print(f'Словарь: {dictText}')
