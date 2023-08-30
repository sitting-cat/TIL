import re
from time import perf_counter

checkPattern = re.compile("^(([a-zA-Z0-9])+)+$")

def getTimeToMatch(subject):
    start = perf_counter()
    checkPattern.match(subject)
    end = perf_counter()

    return end - start


# It takes about 6.1e-6 seconds.
print(getTimeToMatch("abcde"))

# about 8.8e-6 sec.
print(getTimeToMatch("01234567"))

# about 6.4e-4 sec.
print(getTimeToMatch("AbCdEfGh1JkLmN0pQR5Tu"))

# 2.2 sec.
print(getTimeToMatch(
    "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"))

# BUT ...

# It takes 45.1 sec!
# print(testFunction("AAAAAAAAAAAAAAAAAAAAAAAAAAAA@"))

# It takes 720.5 sec!
# print(testFunction("AbCdEfGh1JkLmN0pQR5TuAbCdEfGh1Jk@"))



# See also ...
# https://jvn.jp/jp/JVN86484824/
# https://qiita.com/flat-field/items/f5b0c803ba0b7030d97a
