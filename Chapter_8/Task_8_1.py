class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f'x = {self.x}')
        print(f'y = {self.y}')


point1 = Point(2, 4)
point2 = Point(3, 6)
point3 = Point(4, 8)

print(f'\nОбъект point1:')
point1.show()

print(f'\nОбъект point2:')
point2.show()

print(f'\nОбъект point3:')
point3.show()
