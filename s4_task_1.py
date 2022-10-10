'''
Вычислить число c заданной точностью d

Пример:

- при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}
'''

from decimal import Decimal

def rounding_accuracy(num, d):
    number_in = Decimal(num)
    print(number_in.quantize(Decimal(d)))

number = float(input("Enter a real number: "))
d = input("Enter the required accuracy '0.0001': ")
rounding_accuracy(number, d)