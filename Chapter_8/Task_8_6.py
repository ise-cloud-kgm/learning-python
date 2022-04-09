def create_objects(quantity: int) -> list:
    """Создаёт объекты с помощью конструктора класса MyClass.

    Args:
        quantity (int): Количество создаваемых объектов.

    Returns:
        list[MyClass]: Возвращает список из экземпляров класса MyClass.
    """
    objects = []

    for i in range(quantity):
        obj = MyClass(2 * i + 1, 'Object' + str(i + 1))
        objects.append(obj)

    return objects


def show_objects(quantity: int, objects: list) -> None:
    """Вызывает метод show() для всех объектов."""
    for k in range(quantity):
        objects[k].show()


class MyClass:

    def __init__(self, number: int, name: str) -> None:
        """Создаёт поля для экземпляра класса.

        Args:
            number (int): Целочисленное нечётное значение.
            name (str): Имя экземпляра класса.
        """
        self.number = number
        self.name = name

    def show(self) -> None:
        """Выводит информацию об экземпляре класса."""
        print(f'{self.name} с полем number, равным {self.number}')


amount = int(input('\nВведите количество создаваемых объектов: '))
instances = create_objects(amount)
show_objects(amount, instances)
