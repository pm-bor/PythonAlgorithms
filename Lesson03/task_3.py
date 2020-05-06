"""
Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.

Пример:
В данном массиве чисел максимальное число   88 стоит на
0 позиции, а минимальное число  -49 стоит на    6 позиции
Заменяем их
[88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
В данном массиве чисел максимальное число   88 стоит на
6 позиции, а минимальное число  -49 стоит на    0 позиции
[-49, 26, 41, 75, 23, 52, 88, 60, 69, -18]
"""

import random
[range_min, range_max] = [-100, 100]
# формируем массив случайных не повторяющихся чисел
ar = []
for i in range (10):
    while True:
        x = random.randint(range_min, range_max)
        if not x in ar:
            ar.append(x)
            break
s = ''
for i in ar:
    s += "%+3s " % i
print (s)
i_max = ar.index(max(ar))
i_min = ar.index(min(ar))
s = ''
for i in range(10):
    if i == i_max: s+='max '
    elif i == i_min: s += 'min '
    else: s += "    "
print (s)
if i_max > i_min:
    i_start = i_min
    i_finish = i_max
else:
    i_start = i_max
    i_finish = i_min
s = ''
for i in range(10):
    if i == i_start: s+=f' |<-'
    elif i == i_finish: s += f'>|  '
    elif i_start < i < i_finish: s += f'-'*4
    else: s += "    "
print (s)
s = ''
for i in range(10):
    if i == i_max: s+='min '
    elif i == i_min: s += 'max '
    else: s += "    "
print (s)
[ar[i_max], ar[i_min]] = [ar[i_min], ar[i_max]]
s = ""
for i in ar:
    s += "%+3s " % i
print (s)