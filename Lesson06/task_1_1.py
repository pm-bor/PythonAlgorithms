from functools import reduce
from memory_profiler import profile
"""
Для профилировщика памяти взял следующую задачу:
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
import math
import timeit

@profile
def easy(i):
    c = 1
    n = 2
    while c <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if c == i:
                break
            c += 1
        n += 1
    return n

@profile
def erato (n):
    n_orig = n
    tab = list(zip((168, 1229, 9592, 78498, 664579, 5761455, 24400000), (6, 9, 11, 13, 15, 18, 19)))
    for t in tab:
        if n < t[0]:
            n *= t[1]
            break
    if n == n_orig: return -1
    # только для нечетных чисел
    r = [False] * (n // 2 + 1)
    c = 1 # счетчик найденных чисел
    # Наименьший делитель числа не больше чем корень из этого числа.
    l = int(math.sqrt(n) // 2)
    for i in range(1, l):
        if r[i] == False:
            c += 1
            step = i * 2 + 1
            r[i + step : : step] = [True] * len(r[i + step : : step])
    # дальше идем по оставшейся части последовательности и ещем нужное по порядку число
    for i in range(l, n):
        if r[i] == False:
            c += 1
            if c == n_orig: return i * 2 + 1
    return 0


@profile
def erato_int (n):
    n_orig = n
    tab = list(zip((168, 1229, 9592, 78498, 664579, 5761455, 24400000), (6, 9, 11, 13, 15, 18, 19)))
    for t in tab:
        if n < t[0]:
            n *= t[1]
            break
    if n == n_orig: return -1
    r = [0] * (n // 2 + 1)
    c = 1
    l = int(math.sqrt(n) // 2)
    for i in range(1, l):
        if r[i] == False:
            c += 1
            step = i * 2 + 1
            r[i + step : : step] = [1] * len(r[i + step : : step])
    for i in range(l, n):
        if r[i] == 0:
            c += 1
            if c == n_orig: return i * 2 + 1
    return 0

easy(100)
erato(10000)
erato_int(10000)
"""
Line #    Mem usage    Increment   Line Contents
================================================
    11     13.3 MiB     13.3 MiB   @profile
    12                             def easy(i):
    13     13.3 MiB      0.0 MiB       c = 1
    14     13.3 MiB      0.0 MiB       n = 2
    15     13.3 MiB      0.0 MiB       while c <= i:
    16     13.3 MiB      0.0 MiB           t = 1
    17     13.3 MiB      0.0 MiB           is_simple = True
    18     13.3 MiB      0.0 MiB           while t <= n:
    19     13.3 MiB      0.0 MiB               if n % t == 0 and t != 1 and t != n:
    20     13.3 MiB      0.0 MiB                   is_simple = False
    21     13.3 MiB      0.0 MiB                   break
    22     13.3 MiB      0.0 MiB               t += 1
    23     13.3 MiB      0.0 MiB           if is_simple:
    24     13.3 MiB      0.0 MiB               if c == i:
    25     13.3 MiB      0.0 MiB                   break
    26     13.3 MiB      0.0 MiB               c += 1
    27     13.3 MiB      0.0 MiB           n += 1
    28     13.3 MiB      0.0 MiB       return n

Во время выполенния программы с обычным алгоритмом дополнительного выделения заметного объема памяти не происходит.
В алгоритме существуют всего три переменные, с которыми и производятся вычисления.
Не удалось дождаться окончания работы для 1000 числа, что говорит о том, 
    что профилировщик значительно замедляет время выполнения.
 
Line #    Mem usage    Increment   Line Contents
================================================
    30     13.3 MiB     13.3 MiB   @profile
    31                             def erato (n):
    32     13.3 MiB      0.0 MiB       n_orig = n                             
    41     13.3 MiB      0.0 MiB       tab = list(zip((168, 1229, 9592, 78498, 664579, 5761455, 24400000), (6, 9, 11, 13, 15, 18, 19)))
    42     13.3 MiB      0.0 MiB       for t in tab:
    43     13.3 MiB      0.0 MiB           if n < t[0]:
    44     13.3 MiB      0.0 MiB               n *= t[1]
    45     13.3 MiB      0.0 MiB               break
    46     13.3 MiB      0.0 MiB       if n == n_orig: return -1
    48     13.6 MiB      0.2 MiB       r = [False] * (n // 2 + 1)
    49     13.6 MiB      0.0 MiB       c = 1 # счетчик найденных чисел
    51     13.6 MiB      0.0 MiB       l = int(math.sqrt(n) // 2)
    52     13.7 MiB      0.0 MiB       for i in range(1, l):
    53     13.7 MiB      0.0 MiB           if r[i] == False:
    54     13.7 MiB      0.0 MiB               c += 1
    55     13.7 MiB      0.0 MiB               step = i * 2 + 1
    56     13.7 MiB      0.1 MiB               r[i + step : : step] = [True] * len(r[i + step : : step])
    58     13.7 MiB      0.0 MiB       for i in range(l, n):
    59     13.7 MiB      0.0 MiB           if r[i] == False:
    60     13.7 MiB      0.0 MiB               c += 1
    61     13.7 MiB      0.0 MiB               if c == n_orig: return i * 2 + 1
    62                                 return 0

Во время формирования массива с признаками числового ряда происходит выделение значительного объема памяти.
Видно, что память потребовалась и для генерации цикла заполнения ряда.  
Кроме того, создается достаточно большой массив для присвоения нарезке из ряда значений [True]. 
    Последний рост можно практически свести к нулю, сделав цикл по требуемым значениям, но работает это чуть медленнее. 


Line #    Mem usage    Increment   Line Contents
================================================
    65     13.4 MiB     13.4 MiB   @profile
    66                             def erato_int (n):
    67     13.4 MiB      0.0 MiB       n_orig = n
    76     13.4 MiB      0.0 MiB       tab = list(zip((168, 1229, 9592, 78498, 664579, 5761455, 24400000), (6, 9, 11, 13, 15, 18, 19)))
    77     13.4 MiB      0.0 MiB       for t in tab:
    78     13.4 MiB      0.0 MiB           if n < t[0]:
    79     13.4 MiB      0.0 MiB               n *= t[1]
    80     13.4 MiB      0.0 MiB               break
    81     13.4 MiB      0.0 MiB       if n == n_orig: return -1
    82     13.6 MiB      0.2 MiB       r = [0] * (n // 2 + 1)
    83     13.6 MiB      0.0 MiB       c = 1
    84     13.6 MiB      0.0 MiB       l = int(math.sqrt(n) // 2)
    85     13.8 MiB      0.0 MiB       for i in range(1, l):
    86     13.8 MiB      0.0 MiB           if r[i] == False:
    87     13.8 MiB      0.0 MiB               c += 1
    88     13.8 MiB      0.0 MiB               step = i * 2 + 1
    89     13.8 MiB      0.2 MiB               r[i + step : : step] = [1] * len(r[i + step : : step])
    90     13.8 MiB      0.0 MiB       for i in range(l, n):
    91     13.8 MiB      0.0 MiB           if r[i] == 0:
    92     13.8 MiB      0.0 MiB               c += 1
    93     13.8 MiB      0.0 MiB               if c == n_orig: return i * 2 + 1
    94                                 return 0
    
    Сделал вариант с заполнением не True|False, а int 1|0. 
    И если объем памяти для первоначальной инициализации не изменился, 
        то присвоение новых значений выборке потребовало в двое больший ресурс. 
"""