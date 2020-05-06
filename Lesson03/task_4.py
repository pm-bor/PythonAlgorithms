"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

import random

ar = [random.randint(0, 50) for i in range(50)]
print(ar)
v = max(ar, key=ar.count)
print(f"Число {v} встречается раз: {ar.count(v)}")

