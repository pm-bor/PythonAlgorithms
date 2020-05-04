"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
"""

def calc(x):
    for j in range(1, x + 1):
        sum = 0
        for i in range(1, j + ):
            sum += i
        eq = i * (i + 1) / 2
        print("%+2s: %+5s" % (i, sum == eq))

try:
    n = int(input("Введите число "))
    calc(n)
except ValueError:
    print("Ошибка")
