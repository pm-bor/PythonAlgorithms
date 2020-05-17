"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

"""
Взял задачу 7:
Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
"""
import timeit
import random

# цикл
def calc(x):
    # for j in range(1, x + 1):
        sum = 0
        for i in range(1, x):
            sum += i
        eq = i * (i + 1) / 2
        return sum == eq

# генератор
def calc_gen(x):
    return sum(range(x + 1)) == x * (x + 1) / 2

# цикл
def calc_loop(x):
    even = odd = 0
    while x != 0:
        last = x % 10
        if last % 2 == 0: even += 1
        else: odd += 1
        x = x // 10
    return even, odd



n = 100000
print (calc_gen(n))
print(
    timeit.timeit("calc(n)", setup="from __main__ import calc, n", number=1000))
print(
    timeit.timeit("calc_gen(n)", setup="from __main__ import calc_gen, n", number=1000))
"""
У алгоритмов O(n) – линейная сложность. Несмотря на это, время выполнения различается в два раза.  
9.4452717 цикл
4.3471900 генератор
Генераторы с агрегирующей функцией быстрее циклов 
"""
