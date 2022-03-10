def change_string(string_before: str, *numbers: int) -> str:
    """Изменяет строку-аргумент в соответствии с условием задачи:
    целочисленные аргументы, переданные в функцию, определяют индексы
    букв, которые необходимо включить в строку-результат.

    :param string_before: исходная строка для изменений
    :type string_before: str

    :rtype: str
    :return: строка, состоящая из букв, индексы которых были переданы в функцию
    """
    string_after = ''
    indexes = list(numbers)

    for index in indexes:
        string_after += string_before[index]

    return string_after


text = 'Дикобразы, идущие по холодной пустыне.'

print(f'\nСтрока до изменений: "{text}"\n')

print(f'Изменённая строка 1 раз: {change_string(text, 5, 6, 7)}')
print(f'Изменённая строка 2 раз: {change_string(text, 2, 3, 4, 5 ,6)}')
print(f'Изменённая строка 3 раз: {change_string(text, 3, 4, 5, 6, 7)}')
