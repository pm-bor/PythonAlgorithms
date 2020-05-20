# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы.
import statistics
from random import randint
import collections
import timeit

def mediana_sort(items):
    items.sort
    return items[5]

def mediana_stat(items):
    return statistics.median(items)

def sort_start():
    for _ in range (10000):
        items = [randint(1, 100) for _ in range(11)]
        median = mediana_sort(items)

def stat_start():
    for _ in range (10000):
        items = [randint(1, 100) for _ in range(11)]
        median = mediana_stat(items)

print(timeit.timeit("sort_start()", setup="from __main__ import sort_start", number=10))
print(timeit.timeit("stat_start()", setup="from __main__ import stat_start", number=10))