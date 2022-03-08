def del_longest_and_shortest_word(user_text):
    words = user_text.split()

    max_len_word = max(words, key=len)
    min_len_word = min(words, key=len)

    words.remove(max_len_word)
    words.remove(min_len_word)

    return ' '.join(words)


text = input('\nВведите текст: ')
print(f'Текст после удаления самого длинного и короткого слова: '
      f'{del_longest_and_shortest_word(text)}')
