"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

"""

import collections

def hexchr_to_int(x): return '0123456789ABCDEF'.find(x)

def int_to_hexchr(x): return '0123456789ABCDEF'[x]

def sum_hexchr(x, y, additional):
    s = sum (map(hexchr_to_int, [x, y]), additional)
    return (int_to_hexchr(s - 16), 1) if s > 15 else (int_to_hexchr(s), 0)

def hex_sum(x, y):
    if len(x) != len(y):
        if len(x) > len(y):
            for i in range(len(x) - len(y)):
                y.appendleft("0")
        else:
            for i in range(len(y) - len(x)):
                x.appendleft("0")
    additional = 0
    s = collections.deque()
    for i in range(len(x) - 1, -1, -1):
        n, additional = sum_hexchr(x[i], y[i], additional)
        s.appendleft(n)
    if additional == 1:
        s.appendleft(additional)
    return s

def hex_multi(x, y):
    x = "".join([i for i in x])
    y = "".join([i for i in y])
    s = hex((int(float.fromhex(x) * float.fromhex(y)))).upper()
    result = collections.deque(s[2:])
    return result

# x = collections.deque(input("Первое число: "))
# y = collections.deque(input("Второе число: "))
x = collections.deque("A2")
y = collections.deque("C4F")
print(x, y)
print("Сумма:", hex_sum(x, y))
print("Произведение:", hex_multi(x, y))
