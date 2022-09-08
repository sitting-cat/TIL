value = 5

bad = [x for x in [range(value)] + [range(value, 0, -1)]]
# -> [range(0, 5), range(5, 0, -1)]

good = [x for x in list(range(value)) + list(range(value, 0, -1))]
# -> [0, 1, 2, 3, 4, 5, 4, 3, 2, 1]