numValue = int(input("? >"))
values = [int(input("{0} >".format(x))) for x in range(numValue)]

print("Max : {0}".format(max(values)))
print("Min : {0}".format(min(values)))
print("Sum : {0}".format(sum(values)))
