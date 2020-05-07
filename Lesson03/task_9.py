"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

Пример:

Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
 36 20 42 38
 46 27  7 33
 13 12 47 15
[13, 12, 7, 15] минимальные значения по столбцам
Максимальное среди них = 15
"""

from random import randint

c_min = 4
range_v_size = 5
range_g_size = 10
range_max = 100
range_min = 1

ar = [[randint(range_min, range_max) for j in range(range_g_size)] for i in range(range_v_size)]
print("\n".join(" ".join("%+3s" % i for i in j) for j in ar))
print("-" * 4 * range_g_size + " min ")
ar_min = [min(i) for i in [[row[i] for row in ar] for i in range(range_g_size)]]
print(" ".join("%+3s" % i for i in ar_min))
maximum = ar_min.index(max(ar_min))
print (" ".join("max " if i == maximum else "   " for i in range(range_g_size)))