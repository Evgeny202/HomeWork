"""
Представьте, что сумма за пользование услугами такси складывается из
базового тарифа в размере $4,00 плюс $0,25 за каждые 140 м поездки.
Напишите функцию, принимающую в качестве единственного параметра
расстояние поездки в километрах и возвращающую итоговую сумму опла-
ты такси.
"""
path = int(input())
s = 4.00
path1 = (path * 1000) // 140
price = s + (path1 * 0.25)
print(price)