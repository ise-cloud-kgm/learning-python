def encrypt_eng_text(eng_text):
    encrypt_text = ''

    for symbol in eng_text:
        if symbol == 'b':
            previousSymbol = ord('z')
        elif symbol == 'a':
            previousSymbol = ord('y')
        else:
            previousSymbol = ord(symbol) - 2
        encrypt_text += chr(previousSymbol)

    return encrypt_text


def decipher_eng_text(eng_text):
    deciphered_text = ''

    for symbol in eng_text:
        if symbol == 'y':
            previousSymbol = ord('a')
        elif symbol == 'z':
            previousSymbol = ord('b')
        else:
            previousSymbol = ord(symbol) + 2
        deciphered_text += chr(previousSymbol)

    return deciphered_text


text = input('\nВведите текст: ')

encryptedText = encrypt_eng_text(text)
print(f'Зашифрованный текст: {encryptedText}')
decipheredText = decipher_eng_text(encryptedText)
print(f'Расшифрованный текст: {decipheredText}')
