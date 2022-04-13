class MyClass:
    def __init__(self):
        """Создаёт поле numbers, которое по умолчанию является списком."""
        self.numbers = []

    def __check(lst: list) -> bool:
        """Проверяет состоит ли список только из целочисленных значений."""
        for elem in lst:
            if not isinstance(elem, int):
                return False
        return True

    def set_numbers(self, lst: list) -> None:
        """Устанавливает поле numbers.

        Создание поле numbers происходит, если все элементы
        списка-аргумента состоят из целочисленных значений.

        """
        if MyClass.__check(lst):
            self.numbers = lst
        else:
            print(f'Не все элементы списка являются значениями типа int')


def create_object(obj1: MyClass, obj2: MyClass) -> MyClass:
    """Создаёт объект с полем numbers.

    Поле numbers является списком и заполняется следующим образом:
    каждый элемент формируется путём суммирования соответствующих
    элементов полей numbers объектов obj1 и obj2.

    """
    new_obj = MyClass()  # Создание нового объекта.

    # У обоих объектов есть поля numbers с целочисленными значениями.
    if obj1.numbers != [] and obj2.numbers != []:
        # Оба объекта были созданы на основе класса MyClass.
        if check_objects(obj1, obj2):
            # Добавлений нулей в поле объекта, где элементов меньше.
            if compare_objects(obj1, obj2):
                obj2.numbers.extend(
                    0 for i in range(len(obj1.numbers) - len(obj2.numbers)))
            else:
                obj1.numbers.extend(
                    0 for i in range(len(obj2.numbers) - len(obj1.numbers)))

            for i in range(len(obj1.numbers)):
                # Добавление элементов в поле-список нового объекта.
                new_obj.numbers.append(obj1.numbers[i] + obj2.numbers[i])

    return new_obj


def check_objects(obj1: MyClass, obj2: MyClass) -> bool:
    """Проверяет относятся ли объекты к классу MyClass."""
    if isinstance(obj1, MyClass) and isinstance(obj2, MyClass):
        return True
    return False


def compare_objects(obj1: MyClass, obj2: MyClass) -> bool:
    """Сравнивает длину полей numbers у объектов."""
    if len(obj1.numbers) > len(obj2.numbers):
        return True
    return False


# Списки для заполнения поля numbers у экземпляров класса.
list1 = [0, 2, 4, 6, 8]
list2 = [1, 3, 5, 7, 9]
list3 = ['1', True, 0, 'something']

# Вывод списков.
print(f'\nСписок для object1: {list1}')
print(f'Список для object2: {list2}')
print(f'Список для object3: {list3}')

# Создание экземпляров класса.
object1 = MyClass()
object2 = MyClass()
object3 = MyClass()


# Работа с объектами object1 и object2.
object1.set_numbers(list1)
object2.set_numbers(list2)

print(f'\nobject1.numbers = {object1.numbers}')
print(f'object2.numbers = {object2.numbers}')

# Создание первого объекта с помощью функции create_object().
objects1_2 = create_object(object1, object2)
print(f'object12.numbers = {objects1_2.numbers}')


# Работа с объектами object1 и object3.
print(f'\nobject1.numbers = {object1.numbers}')
object3.set_numbers(list3)
print(f'object3.numbers = {object3.numbers}')

# Создание второго объекта с помощью функции create_object().
objects1_3 = create_object(object1, object3)
print(f'object13.numbers = {objects1_3.numbers}')


# Работа с объектами object2 и object1_2.
print(f'\nobject2.numbers = {object2.numbers}')
print(f'object12.numbers = {objects1_2.numbers}')

# Создание третьего объекта с помощью функции create_object().
objects2_12 = create_object(object2, objects1_2)
print(f'object2_12.numbers = {objects2_12.numbers}')
