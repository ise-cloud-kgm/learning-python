divisibleByThree = set()
divisibleByFour = set()

for number in range(50):
    if number % 3 == 0:
        divisibleByThree.add(number)
    if number % 4 == 0:
        divisibleByFour.add(number)

print(f'\nЧисла, которые делятся или на 3, или на 4, но при этом не делятся на'
      f' 3 и 4 одновременно:\n{divisibleByThree ^ divisibleByFour}')
