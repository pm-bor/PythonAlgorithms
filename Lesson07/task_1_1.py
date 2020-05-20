# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
from random import randint

def bubble(array):
    for i in range(range_size - 1):
        position = 0
        for j in range(range_size - i - 1):
            if array[j - position] <= array[j + 1]:
                position += 1
                if j == (range_size - i - 2):
                    array.insert(j + 1, array.pop(j - position + 1))
                    position = 0
                    # print(array)
            else:
                if position != 0:
                    array.insert(j, array.pop(j - position))
                    # print(array)
                position = 0
                continue


range_size = 100
array = [randint(-99, 100) for _ in range(range_size)]

print('Исходный:   ', " ".join(["%+3s" % element for element in array]))
bubble(array)
print('По убыванию:', " ".join(["%+3s" % element for element in array]))