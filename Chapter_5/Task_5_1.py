text = '''2 + 2 * 2 = 6
3 + 3 * 3 = 12
4 + 4 * 4 = 20
'''

print(f'\nТекст до изменений:\n{text}')

text = text.replace('*', 'Hello Python')

print(f'Текст после изменений:\n{text}')
