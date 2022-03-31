class MyClass:

    def __init__(self, value1, value2):
        isstring = type(value1) == str and type(value2) == str
        isinteger = type(value1) == int and type(value2) == int

        if isstring or isinteger:
            self.value1 = value1
            self.value2 = value2

    def get_total_value(self):
        if hasattr(self, 'value1') and hasattr(self, 'value2'):
            return self.value1 + self.value2
        return f'Для объекта не будут созданы поля!'

    def show_total_value(self):
        print(f'Результат создания объекта: {self.get_total_value()}')


concatenation = MyClass('Elizabeth', 'II')
summa = MyClass(2, 8)
noResult = MyClass('Elizabeth', 2)

print(f'\nОбъект concatenation:')
concatenation.show_total_value()

print(f'\nОбъект summa:')
summa.show_total_value()

print(f'\nОбъект noResult:')
noResult.show_total_value()
