from datetime import date

date1 = date.fromisoformat(input('\nВведите первую дату: '))
date2 = date.fromisoformat(input('Введите вторую дату: '))

if date1 > date2:
    dateDifference = date1 - date2
else:
    dateDifference = date2 - date1

print(f'Количество полных дней между двумя датами: {dateDifference.days}')
