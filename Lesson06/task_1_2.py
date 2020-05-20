from pympler import tracker
import collections


tr = tracker.SummaryTracker()
tr.print_diff()

class HexNum (object):
    def __init__(self, hex_deque):
        self.num = hex_deque

    def __add__(self, other):
        return hex_sum(self.num, other.num)

    def __repr__(self):
        return str(self.num)

    def __mul__(self, other):
        return hex_multi(self.num, other.num)

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
x = HexNum(collections.deque("A2"))
y = HexNum(collections.deque("C4F"))

print(x, y)
print("Сумма:", x + y)
print("Произведение:", x * y)

tr.print_diff()

"""
Видны все функции, объекты и специальные коллекции. Наследование и перегрузка операторов не занимает много места.
Система хранениня некоторых переменных странная. Иногда при объявлении целых чисел в памяти они будто не появляются.


                     types |   # objects |   total size
========================== | =========== | ============
                      code |           9 |    756     B
         collections.deque |           2 |    640     B
                      type |           1 |    536     B
                      dict |           3 |    340     B
                       str |           5 |    204     B
         getset_descriptor |           2 |     80     B
        function (__add__) |           1 |     72     B
       function (__repr__) |           1 |     72     B
        function (__mul__) |           1 |     72     B
  function (hexchr_to_int) |           1 |     72     B
        function (hex_sum) |           1 |     72     B
      function (hex_multi) |           1 |     72     B
       function (__init__) |           1 |     72     B
  function (int_to_hexchr) |           1 |     72     B
     function (sum_hexchr) |           1 |     72     B

Python 3.7.4
win 10 x64                 
"""