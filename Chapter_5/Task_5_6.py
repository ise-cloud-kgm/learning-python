def decipher_eng_text(eng_text):
    deciphered_text = ''

    for symbol in eng_text:
        if symbol == 'z':
            nextSymbol = ord('a')
        else:
            nextSymbol = ord(symbol) + 1
        deciphered_text += chr(nextSymbol)

    return deciphered_text


text = input('\nВведите текст для расшифровки: ')
print(f'Расшифрованный текст: {decipher_eng_text(text)}')
