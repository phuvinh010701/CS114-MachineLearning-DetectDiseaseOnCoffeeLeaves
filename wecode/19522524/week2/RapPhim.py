n, m, a = [int(i) for i in input().split()]

from math import ceil
print(ceil(n / a) * ceil(m / a))