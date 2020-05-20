# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
from random import randint

def bubble(array):
    for i in range(range_size - 1):
        for j in range(range_size - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

range_size = 100
array = [randint(-99, 100) for _ in range(range_size)]

print('Исходный:   ', " ".join(["%+3s" % element for element in array]))
bubble(array)
print('По убыванию:', " ".join(["%+3s" % element for element in array]))