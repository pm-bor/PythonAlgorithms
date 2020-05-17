"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

namedtuple
"""

import collections
import random

company_names = ['Belka Protein', 'Strelka Art', 'Gagarin Fest', 'Titov and partners']
company_profits = [random.randint(100000,1000000000) for i in range (4 * 4)]
company_quarter_profits = [[name, quarter, random.randint(10000, 100000000) * 40] for quarter in [1, 2, 3, 4] for name in company_names]

company_quarter_profits = collections.namedtuple('Company_quarters', 'Name Q1 Q2 Q3 Q4')

companies = [company_quarter_profits._make([name] + [random.randint(10000, 100000000) * 40] * 4) for name in company_names]

profits = [sum(company[1:4]) for company in companies]
average = round(sum(profits) / len(profits))
print(companies)
print("Годовая прибыль выше средней у компаний:", ", ".join([company_names[i] for i in range(4) if profits[i] >= average]))
print("Годовая прибыль ниже средней у компаний:", ", ".join([company_names[i] for i in range(4) if profits[i] < average]))