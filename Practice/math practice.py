# © Peter Murphy 2019
from fractions import Fraction
def partialsums (i):
    Series = [21/(n(n + 3)) for n in range(1, i +1)]
    print(Series)
    Sum = 0.0
    for n in Series:
        Sum += n
        print(Sum)
    Sum = round(Sum, 3)
    return Fraction(str(Sum))
