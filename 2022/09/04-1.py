from math import ceil, floor

try:
    subjectValue = float(input("? >"))
except ValueError as e:
    raise ValueError("半角数値以外が入力されました") from e


print("切り上げ : {0}".format(ceil(subjectValue)))
print("切り下げ : {0}".format(floor(subjectValue)))
print("四捨五入して整数に : {0}".format(floor(subjectValue + 0.5)))
print("小数点下第二位で四捨五入 : {0}".format(floor(subjectValue * 10 + 0.5) / 10))
