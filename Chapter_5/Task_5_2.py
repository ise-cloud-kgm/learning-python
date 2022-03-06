def replace_star(text):
    if '*' in text:
        for index in range(len(text) - 1):
            if text[index] == '*':
                text = text[:index] + 'А' + text[index + 1:]
        return text
    else:
        return f'В тексте "{text}" нет символа "*"'


text1 = '*лексей поздоровался с *лександром'
text2 = 'Мама мыла раму'

print(f'\nСтрока №1: "{text1}"')
print(f'\tСтрока №1 после изменений:\n{replace_star(text1)}')

print(f'\nСтрока №2: "{text2}"')
print(f'\tСтрока №2 после изменений:\n{replace_star(text2)}')
