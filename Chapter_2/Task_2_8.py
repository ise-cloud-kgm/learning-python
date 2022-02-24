number = int(input('\nВведите целое число от 1 до 7 включительно: '))

while number > 7 or number < 1:
    print('\nВведённое вами число не входит в диапазон [1; 7]')
    number = int(input('Введите число заново: '))

daysOfWeek = {
    1: 'Понедельник',
    2: 'Вторник',
    3: 'Среда',
    4: 'Четверг',
    5: 'Пятница',
    6: 'Суббота',
    7: 'Воскресенье'
}

for day in daysOfWeek.keys():
    if number == day:
        print(f'\nЧислу {number} соответствует день недели - {daysOfWeek[day]}')
        break