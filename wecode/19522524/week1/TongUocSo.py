from math import sqrt
def sum(n):
    if n <= 0:
        return 0
    res = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            res += i
    return res

print(sum(int(input())))