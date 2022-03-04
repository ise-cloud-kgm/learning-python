text = input('\nВведите текст: ')

print()

keysOfDictText = set(text)  # Убираем повторы ключей с помощью множества.
dictText = dict()
index = 0  # Индекс для срезов (для читаемости и сокращения длины строки).

for symbol in keysOfDictText:
    index = text.index(symbol)
    dictText[symbol] = text[:index] + text[index + 1:]

listKeys = list(dictText.keys())  # Список для сортировки словаря по алфавиту.
listKeys.sort()

for key in listKeys:
    print(f'{key}: {dictText[key]}')
