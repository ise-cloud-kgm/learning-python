from typing import List, Optional


def create_object(fields: List, name: Optional[str] = None):

    # Введённое имя класса не является текстовым значением,
    if type(name) != str:
        # поэтому устанавливаем значение по умолчанию для переменной name.
        name = 'Unknown'

    # Если аргумент fields не является списком.
    if type(fields) != list:

        class MyClass:

            def show(self):
                print('\nОбъект без полей')
                print(f'Класс {self.__class__.__name__}')

    # Аргумент fields является списком.
    else:

        class MyClass:

            def __init__(self):
                # Записываем в новый список только текстовые
                # значения из списка fields.
                field_names = list(filter(lambda f_name: type(f_name) == str, fields))

                for field in field_names:
                    # Проверка начинается ли элемент списка на цифру.
                    # Это необходимо, потому что имена полей не могут
                    # начинаться на цифру.
                    if field[:1] in '0123456789':
                        field_names.remove(field)

                count = 1
                for field in field_names:
                    # Создание полей объекта.
                    self.__dict__[field] = count
                    count += 1

            def show(self):
                print(f'\nОбъект с полями:')
                for attr in dir(self):
                    if not attr.startswith('_') and attr != 'show':
                        print(f'{attr} = {self.__dict__[attr]}')
                print(f'Класс {self.__class__.__name__}')

    MyClass.__name__ = name
    return MyClass()


colors = create_object([1, 'red', 2, 'green', 3, 'blue'], 'MyColors')
colors.show()

cars = create_object(['BMW', 'Infinity', 'Audio'], 'Cars')
cars.show()

incognito = create_object([1, 2, '2', 3])
incognito.show()
