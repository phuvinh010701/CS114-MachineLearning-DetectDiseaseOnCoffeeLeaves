f = float(input())

from decimal import *
getcontext().prec = 6
C = (f - 32) / 1.8
K = C + 273.15

print("{} {}".format(Decimal(C).normalize(), Decimal(K).normalize()))