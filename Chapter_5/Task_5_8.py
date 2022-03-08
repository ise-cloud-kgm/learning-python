vowels = ['a', 'e', 'i', 'o', 'u', 'y']
consonants = []

for letter in range(ord('a'), ord('z') + 1):
    if chr(letter) in vowels:
        continue
    consonants.append(chr(letter))  # Заполнение списка согласными буквами.


def encrypt_text(user_text):
    encrypted_text = ''

    for symbol in user_text:
        if symbol in vowels:  # Буква относится к гласным.
            if symbol != vowels[-1]:  # Буква не последняя в списке.
                encrypted_text += vowels[vowels.index(symbol) + 1]
            else:  # Буква последняя в списке.
                encrypted_text += vowels[0]
        else:  # Буква относится к согласным.
            if symbol != consonants[-1]:  # Буква не последняя в списке.
                encrypted_text += consonants[consonants.index(symbol) + 1]
            else:  # Буква последняя в списке.
                encrypted_text += consonants[0]

    return encrypted_text


def decipher_text(encrypted_text):
    deciphered_text = ''

    for symbol in encrypted_text:
        if symbol in vowels:  # Буква относится к гласным.
            if symbol != vowels[0]:  # Буква не первая в списке.
                deciphered_text += vowels[vowels.index(symbol) - 1]
            else:  # Буква первая в списке.
                deciphered_text += vowels[-1]
        else:  # Буква относится к согласным.
            if symbol != consonants[0]:  # Буква не первая в списке.
                deciphered_text += consonants[consonants.index(symbol) - 1]
            else:  # Буква первая в списке.
                deciphered_text += consonants[-1]

    return deciphered_text


text = input('\nВведите текст: ')

encryptedText = encrypt_text(text)
print(f'Текст после шифрования: {encryptedText}')

decipheredText = decipher_text(encryptedText)
print(f'Текст после дешифрования: {decipheredText}')
