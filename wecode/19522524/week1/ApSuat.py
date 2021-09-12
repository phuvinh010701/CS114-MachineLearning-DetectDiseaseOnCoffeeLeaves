PSI=float(input())
from decimal import *
getcontext().prec=6
print(Decimal(0.453592/2.54**2*PSI).normalize())