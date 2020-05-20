# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы.
import statistics
import random
import collections
import timeit

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

def min_n(d, n):
    if n == 1:
        return min(d)
    else:
        d.remove(min(d))
        return min_n(d, n - 1)

def max_n(d, n):
    if n == 1:
        return max(d)
    else:
        d.remove(max(d))
        return max_n(d, n - 1)

def mediana_avg(items):
        half_lenght = (len(items) - 1) // 2
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
        diff = len(bigger) - len(less)
        if abs(diff) <= same:
            return closer_value
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


def brute_start():
    for _ in range (10000):
        items = [randint(1, 1000) for _ in range(63)]
        median = mediana_brute(items)
        # if statistics.median(items) != median:
        #     print(items, mediana_brute(items, True), median, statistics.median(items) == median, statistics.median(items))

def avg_start():
    for _ in range (10000):
        items = [randint(1, 1000) for _ in range(63)]
        median = mediana_avg(items)

print(timeit.timeit("brute_start()", setup="from __main__ import brute_start", number=10))
print(timeit.timeit("avg_start()", setup="from __main__ import avg_start", number=10))

"""
Если на небольших наборах (до 11 элементов) алгоритмы показываеют схожее время выполнения, 
 то с ростом элементов превосходство у "медианы от среднего". При 63 элементах в среднем быстрее более, чем в два раза.  
"""