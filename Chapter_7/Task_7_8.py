from datetime import datetime, time

currentDatetime = datetime.now()
inputTime = time.fromisoformat(input('\nВведите любое время: '))
inputTime = datetime.combine(currentDatetime.date(), inputTime)

print(f'Текущее время: {currentDatetime.time()}')

# Убираем одинаковые даты и оставляем только разницу во времени.
timeDifference = abs(currentDatetime - inputTime)

print(f'Разница между двумя временными промежутками: {timeDifference}')
