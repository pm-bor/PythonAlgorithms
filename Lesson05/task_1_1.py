"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

defaultdict
"""

import collections
import random


company_names = ['Belka Protein', 'Strelka Art', 'Gagarin Fest', 'Titov and partners']
company_quarter_profits = [[name, quarter, random.randint(10000, 100000000) * 40] for quarter in [1, 2, 3, 4] for name in company_names]

company_annual_profits = collections.defaultdict(int)
for name, quarter, profit in company_quarter_profits:
    company_annual_profits[name] += profit

average_annual_profit = round(sum(company_annual_profits.values()) / len(company_annual_profits))

print (company_quarter_profits)

print("Годовая прибыль выше средней у компаний:", ", ".join([name for name, profit in company_annual_profits.items() if profit >= average_annual_profit]))
print("Годовая прибыль ниже средней у компаний:", ", ".join([name for name, profit in company_annual_profits.items() if profit < average_annual_profit]))