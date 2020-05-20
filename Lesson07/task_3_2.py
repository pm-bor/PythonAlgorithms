# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы.
import statistics
import random
import collections

from random import randint

def min_n(d, n):
    if n == 1:
        return min(d)
    else:
        try:
            d.remove(min(d))
            return min_n(d, n - 1)
        except:
            print (d)

def max_n(d, n):
    if n == 1:
        return max(d)
    else:
        try:
            d.remove(max(d))
            return max_n(d, n - 1)
        except:
            print(d)


def mediana_avg(items, show=False):
    half_lenght = (len(items)- 1) // 2
    average = sum(items) / len(items)
    closer_value = min(items, key=lambda x: abs(average - x))
    bigger = collections.deque()
    less = collections.deque()
    same = 0
    for item in items:
        if item > closer_value:
            if len(bigger) == 0 or item <= bigger[0]:
                bigger.appendleft(item)
            else:
                bigger.append(item)
        elif item < closer_value:
            if len(less) == 0 or item >= less[0]:
                less.appendleft(item)
            else:
                less.append(item)
        else:
            same += 1
    same -= 1
    if show: print (closer_value, same, bigger, less, min(bigger))
    diff = len(bigger) - len(less)
    if abs(diff) <= same:
        return  closer_value
    else:
        if diff == 2 + same:
            return bigger[0]
        elif diff == -2 - same:
            return less[0]
        elif diff > 0:
            bigger.popleft()
            return min_n(bigger, len(bigger) - half_lenght)
        elif diff < 0:
            less.popleft()
            return max_n(less, len(less) - half_lenght)


for _ in range (10000):
    items = [randint(1, 100) for _ in range(11)]
    median = mediana_avg(items)
    if statistics.median(items) != median:
        print(items, mediana_avg(items, True), median, statistics.median(items) == median, statistics.median(items))