def reverse_words(user_text):
    words = user_text.split()
    words.reverse()
    return ' '.join(words)


text = input('\nВведите текст: ')
print(f'Текст, в котором слова расположены в обратном порядке: '
      f'{reverse_words(text)}')
