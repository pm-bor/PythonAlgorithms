"""
Задание_8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки
и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.

1-я строка:
3
3
3
3
2-я строка:
3
3
3
3
3-я строка:
3
3
3
3
4-я строка:
3
3
3
3
5-я строка:
3
3
3
3

[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
"""

from random import randint

range_v_size = 5
range_g_size = 4
range_max = 100
range_min = -99

# раскомментаровать, чтобы массив заполнялся случайными числами
# mode_type = 'auto'

# было интересно попробовать реализовать в одну строчку
# print("\n".join(" ".join("%+3s" % i for i in j) + " %+5s" % sum(j) for j in [[randint(-99, 100) for j in range(4)] for i in range(5)]))
print("\n".join(" ".join("%+3s" % i for i in j) + " %+5s" % sum(j) for j in [[int(input("Строка %d - Элемент %d: " % (i + 1, j + 1))) for j in range(4)] for i in range(5)]))

if 'mode_type' in vars():
    ar = [[randint(range_min, range_max) for j in range(range_g_size)] for i in range(range_v_size)]
else:
    ar = []
    for i in range(range_v_size):
        print (f"{i+1} строка:")
        row = [int(input()) for j in range(range_g_size)]
        ar.append(row)
print("\n".join(" ".join("%+3s" % i for i in j) + " %+5s" % sum(j) for j in ar))