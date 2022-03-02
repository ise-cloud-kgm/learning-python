vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
uppercaseVowels = {'А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я'}

text = input('\nВведите текстовое значение на русском языке: ')
setText = set(text)

vowelsInText = (setText & vowels) | (setText & uppercaseVowels)

print(f'Гласные, которые содержатся в вашем тексте: {vowelsInText}')
