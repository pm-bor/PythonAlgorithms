# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы.
import statistics
import random
import timeit

from random import randint

def mediana_brute(items):
    # print (items)
    for i, value in enumerate(items):
        bigger = less = same = 0
        for j in items[:i] + items[i+1:]:
            if j < value:
                less += 1
            elif j > value:
                bigger += 1
            else:
                same += 1
        if abs(less - bigger) <= same:
            return value

def brute_start():
    for _ in range (10000):
        items = [randint(1, 1000) for _ in range(15)]
        median = mediana_brute(items)


print(timeit.timeit("brute_start()", setup="from __main__ import brute_start", number=10))