"""
Задание_6.	В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

Подсказки:
1) берем первый минимальный и максимальный
2) не забудьте, что сначала может быть минимальный, потом максимальный
а может - наоборот. во всех этих случаях нужна корректная работа

Пример:
Введите количество элементов в массиве: 10
Массив: [88, 58, 50, 77, 49, 6, 42, 67, 14, 79]
Сумма элементов между минимальным (6)  и максимальным (88) элементами: 234
"""

from random import randint

import random
[range_size, range_min, range_max] = [20, -99, 100]
# формируем массив случайных не повторяющихся чисел
ar = []
for i in range (range_size):
    while True:
        x = random.randint(range_min, range_max)
        if not x in ar:
            ar.append(x)
            break
s = ''
for i in ar:
    s += " %+3s  " % i
print (s)
i_max = ar.index(max(ar))
i_min = ar.index(min(ar))
if i_max > i_min:
    i_start = i_min
    i_finish = i_max
else:
    i_start = i_max
    i_finish = i_min
s = ''
for i in range(range_size):
    if i in (i_start, i_finish):
        if i == i_finish: s+='|'
        if i == i_start: s+=' '
        if i == i_max: s += "max"
        if i == i_min: s += 'min'
        if i == i_finish: s+='  '
        if i == i_start: s+='|+'
    elif i_start < i < i_finish:
        s += "+" * 6
    else: s += "      "
print (s)
if len (ar [i_start:i_finish - 1]) == 0:
    print ("Нет чисел между экстремальными значениями")
else:
    s = ''
    for i in range(range_size):
        if i_start < i < i_finish - 1:
            s += " %+3s +" % ar[i]
        elif i == i_finish - 1:
            s += " %+3s = " % ar[i]
            break
        else: s += "      "
    s += str(sum(ar[i_start+1:i_finish]))
    print (s)