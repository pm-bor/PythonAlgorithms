"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

"""
Взял задачу 2:	
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""
import timeit
import random

# цикл
def calc_loop(x):
    even = odd = 0
    while x != 0:
        last = x % 10
        if last % 2 == 0: even += 1
        else: odd += 1
        x = x // 10
    return even, odd


# рекурсия
def calc(x, even=0, odd=0):
    if x == 0:
        return even, odd
    else:
        last = x % 10
        x = x // 10
        if last % 2 == 0:
            even += 1
            return calc(x, even, odd)
        else:
            odd += 1
            return calc(x, even, odd)


# итератор

# движение по цифрам целого числа, начиная с последней
def int_iter_rev(x):
    while x != 0:
        last = x % 10
        x = x // 10
        yield last


def calc_gen(x, even=0, odd=0):
    odd = sum (1 for i in int_iter_rev(x) if i % 2 != 0)
    even = len(str(x)) - odd
    return even, odd


# анализ строки
def calc_str_loop(x):
    odd = even = 0
    for i in x:
        # первоначальный вариант убран из-за двух проверок
        #  odd += 1 if i in [1,3,5,7,9] else 0
        # even += 1 if i in [0,2,4,6,8] else 0
        if i in (1,3,5,7,9): odd += 1
        else: even += 1
    return even, odd


# анализ строки генератором
def calc_str_gen(x):
    odd = sum(1 for s in x if s in (1, 3, 5, 7, 9))
    return len(x) - odd, odd



n = random.randint(100000000000000000, 999999999999999999)

print(
    timeit.timeit("calc_loop(n)", setup="from __main__ import calc_loop, n", number=1000))
print(
    timeit.timeit("calc(n)", setup="from __main__ import calc, n", number=1000))
print(
    timeit.timeit("calc_gen(n)", setup="from __main__ import calc_gen, n", number=1000))
n = str(n)
print(
    timeit.timeit("calc_str_loop(n),", setup="from __main__ import calc_str_loop, n", number=1000))
print(
    timeit.timeit("calc_str_gen(n),", setup="from __main__ import calc_str_gen, n", number=1000))

"""
У алгоритмов O(n) – линейная сложность. Несмотря на это, время выполнения различается значительно.  
5 вариантов
0.00952 1 цикл 
0.01229 2 рекурсия
0.01387 3 итератор
0.00445 4 анализ строки
0.00351 5 анализ строки с генератором
рейтинг: 5 4 1 2 3
1. "Отправной вариант"
2. Увеличенный стек рекурсивных вызовов несет дополнительные накладные расходы   
3. Встроенные итераторы работают быстрее самодельных. 
    Отдельный генератор для четных и нечетных чисел в два раза увеличивал время выполнения. 
    Заменил на вычисление разности между количеством цифр в числе и найденным количеством четных   
4. Встроенные функции анализа строки работают достаточно быстро. Происходит сопоставление без дополнительных вычислений.
5. Генераторы с агрегирующей функцией быстрее циклов, нет отдельной переменной для четных чисел 

Есть идея посимвольно считывать ввод пользователя, подсчитывая на лету. 
Удалось пока только в терминале реализовать через msvcrt.getch().
"""
