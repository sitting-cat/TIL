numValue = int(input("? >"))

result = 0
for x in range(numValue):
    value = int(input("{0} >".format(x)))
    result += value if value < numValue else 0