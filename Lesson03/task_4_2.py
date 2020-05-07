"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

import random
from collections import Counter

# слово с окончанием в зависимости от числа
def ending(n, word, e1, e2, e3 = None):
    if e3 == None: e3 = e2
    if n < 0: n *= -1
    if n < 5 or n > 20:
        d = n % 10
        if d == 1: return word + e1
        elif 2 <= d <= 4: return word + e2
        else: return word + e3
    else:
        return word + e3

ar = [random.randint(1, 50) for i in range(50)]
print(' '.join(str(i) for i in ar))
c = Counter(ar)
m = max(c.values())
m_numbers = [k for k, v in c.items() if v == m]
l = len(m_numbers)
print(f"{ending(l, 'Чис', 'ло', 'ла', 'ел')} {m_numbers} {ending(l, 'встреча', 'ется', 'ются')} {m} {ending(m, 'раз', '', 'а', '')}")

