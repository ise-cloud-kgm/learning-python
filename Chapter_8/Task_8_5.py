def create_object_with_int_fields(obj):

    class IntFields:

        def __init__(self):
            # Проходимся в цикле по каждому атрибуту объекта obj.
            for attribute, value in obj.__dict__.items():
                # Если значение атрибута является целочисленным, то
                if type(value) == int:
                    # добавляем это поле к полям класса IntFields.
                    self.__dict__[attribute] = value

        def show(self):
            print(f'\nЭкземпляр класса "{obj.__class__.__name__}" с полями:')
            # Проходимся в цикле по каждому атрибуту объекта, созданного с
            # помощью функции create_object_with_int_fields().
            for attribute in dir(self):
                # Если атрибут не начинается с нижнего подчёркивание (то есть
                # это не специальный метод) и атрибут не является методом show().
                if not attribute.startswith('_') and attribute != 'show':
                    print(f'{attribute} = {self.__dict__[attribute]}')

    return IntFields()


class Person:
    """Класс 'Человек' для проверки функции create_object_with_int_fields()."""

    def __init__(self):
        self.name = 'Alexander'
        self.arms = 2
        self.legs = 2


class Cat:
    """Класс 'Кот' для проверки функции create_object_with_int_fields()."""

    def __init__(self):
        self.nickname = 'Barsik'
        self.paws = 4
        self.tail = True


person = Person()
person = create_object_with_int_fields(person)
person.show()

cat = Cat()
cat = create_object_with_int_fields(cat)
cat.show()
