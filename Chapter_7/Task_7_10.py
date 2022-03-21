fileName = input('\nВведите имя создаваемого файла: ')

print(f'\nВведите текст для созданного вами файла:')
with open(fileName, 'w', encoding='utf-8') as file:
    file.write(input().swapcase())
    file.close()

print(f'\nВаш текст изменён:')
with open(fileName, 'r', encoding='utf-8') as file:
    print(file.read())
    file.close()
