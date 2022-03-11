def get_months():
    """Перебирает все месяцы."""
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    for month in months:
        yield month


months = get_months()

print(f'\nOutput all months with the generator {months.__name__}: ')

for month in months:
    print(month, end=' ')

print()
