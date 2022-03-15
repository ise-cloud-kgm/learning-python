def bread(f):
    def wrapper(n):
        print('</______\>')
        for i in range(n):
            f()
        print('<\______/>')

    return wrapper


@bread
def sandwich(food="~~~~~~~~~~"):
    print(food)


N = 3

print()
sandwich(N)
