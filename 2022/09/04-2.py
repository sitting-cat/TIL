from typing import List

subjects: List[str] = input("? >").split()

if not len(subjects):
    subjects = [
        "apple",
        "banana",
        "cherry",
        "grape",
        "kiwifruit",
        "lemon",
        "mango",
        "melon",
        "orange",
        "peach"
    ]


# bool値のリストを生成し、Trueは1・Falseは0としてsum関数で合計する
result = sum(('a' in subject) for subject in subjects)

print("aを含む要素は{0}個あった".format(result))
