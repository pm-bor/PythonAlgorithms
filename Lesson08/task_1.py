"""
1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
import hashlib

new_string = input("Введите строку из маленьких латинских букв: ")

sub_strings = set()

for i in range(len(new_string)):
    for j in range(len(new_string) - 1 if i == 0 else len(new_string), i, -1):
        sub_strings.add(hashlib.sha1(new_string[i:j].encode('utf-8')).hexdigest())

print("Разых подстрок:", len(sub_strings))

"""
Введите строку из маленьких латинских букв: faf
Разых подстрок: 4
"""