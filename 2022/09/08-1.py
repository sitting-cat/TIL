from itertools import product

hight = 5
width = 8

# Bad
for x in range(width):
    for y in range(hight):
        print(x, y)

# Good
for x, y in product(range(width), range(hight)):
    print(x, y)
