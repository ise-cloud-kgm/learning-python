# Кортеж, состоящий из имён файлов, для проверки вводимого имени файла.
files = ('citation.txt', 'poem.txt', 'song.txt')


def stars(some_description: callable):
    """Оборачивает функцию с описанием задачи символами '*'."""
    def wrapper():
        print(f'\n\t', '*' * 3, end=' ')
        some_description()
        print('*' * 3, '\n')

    return wrapper


@stars
def description():
    """Выводит описание задачи."""
    print('Введите полное имя одного из предложенных файлов.', end=' ')


def print_filenames():
    """Выводит имена существующих файлов."""
    for i in range(len(files)):
        print(f'\t\t {i + 1} файл - {files[i]}')


def print_file_content(file_name: str):
    """Выводит содержимое файла."""
    print(f'\n\tСодержимое {file_name}:')
    file = open(file_name, 'r', encoding='utf-8')
    print(file.read())
    file.close()


def create_file_with_row_numbers(file_name: str):
    """Создаёт файл с нумерацией строк на основе файла без строк."""
    new_file = open(f'copy_{file_name}', 'w', encoding='utf-8')

    index_row = 1
    file = open(file_name, 'r', encoding='utf-8')
    for row in file:
        new_file.write(f'[{index_row}] {row}')
        index_row += 1

    file.close()
    new_file.close()


def print_file_with_row_numbers(file_name: str):
    """Выводит новый файл с пронумерованными строками."""
    print(f'\n\tСодержимое {file_name}:')
    file = open(f'copy_{file_name}', 'r', encoding='utf-8')
    print(file.read())
    file.close()


description()  # Вывод описания задачи.
print_filenames()  # Вывод имён файлов.

fileName = input('\nВведите имя файла: ')

# Проверка, ввёл ли пользователь существующее имя файла.
while fileName not in files:
    print(f'\nВведённого вами файла нет среди предложенных!')
    fileName = input('\nВведите имя файла: ')

# Вывод содержимого файла.
print_file_content(fileName)
# Создание нового файла с пронумерованными строками.
create_file_with_row_numbers(fileName)
# Вывод нового файла с пронумерованными строками.
print_file_with_row_numbers(fileName)
