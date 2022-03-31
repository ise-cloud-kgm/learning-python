class List:

    def __init__(self, some_list):
        self.numbers = some_list

    def get_list_of_int_numbers(self):
        for item in self.numbers:
            if type(item) != int:
                self.numbers.remove(item)

    def show(self):
        print(f'Список из целочисленных элементов: {self.numbers}')

    def compute_average_value(self):
        return sum(self.numbers) / len(self.numbers)


# Исходные списки, на основе которых будут получены списки,
# состоящие из целочисленных элементов.
list1 = ['Jake', 1, 'Justin', 2, 'John', 3]
list2 = [True, 4, False, 5, 5.5, 6]
list3 = [(1, 2), 7, {1: 2}, 8, [1, 2], 9]

object1 = List(list1)
object2 = List(list2)
object3 = List(list3)

print(f'\nИсходный список: {list1}')
print(f'\nОбъект object1:')
object1.get_list_of_int_numbers()
object1.show()
print(f'Среднее значение: {object1.compute_average_value()}')

print(f'\nИсходный список: {list2}')
print(f'\nОбъект object2:')
object2.get_list_of_int_numbers()
object2.show()
print(f'Среднее значение: {object2.compute_average_value()}')

print(f'\nИсходный список: {list3}')
print(f'\nОбъект object3:')
object3.get_list_of_int_numbers()
object3.show()
print(f'Среднее значение: {object3.compute_average_value()}')
