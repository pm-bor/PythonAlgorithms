# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы.
import statistics
import random

from random import randint

def mediana_brute(items):

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

for _ in range (10):
    items = [randint(1, 100) for _ in range(11)]
    median = mediana_brute(items)
    if statistics.median(items) != median:
        print(items, mediana_brute(items, True), median, statistics.median(items) == median, statistics.median(items))
# print(median, statistics.median(items) == median)