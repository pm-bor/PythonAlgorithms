# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
from random import randint
import timeit


def b(array):
    for i in range(range_size - 1):
        for j in range(range_size - i - 1):
            # print (array)
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

def bubble(array):
    for i in range(range_size - 1):
        position = 0
        any_flip = False
        for j in range(range_size - i - 1):
            if array[j - position] <= array[j + 1]:
                position += 1
                if j == (range_size - i - 2):
                    array.insert(j + 1, array.pop(j - position + 1))
                    any_flip = True
                    position = 0
                    # print(array)
            else:
                if position != 0:
                    pass
                    array.insert(j, array.pop(j - position))
                else:
                    if any_flip == False:
                        break
                # print(array)
                position = 0


range_size = 100
array = [randint(-99, 100) for _ in range(range_size)]
print('Исходный:   ', " ".join(["%+3s" % element for element in array]))
print(timeit.timeit("b(array)", setup="from __main__ import b, array", number=100))
array = [randint(-99, 100) for _ in range(range_size)]
print(timeit.timeit("bubble(array)", setup="from __main__ import bubble, array", number=100))
print('По убыванию:', " ".join(["%+3s" % element for element in array]))
