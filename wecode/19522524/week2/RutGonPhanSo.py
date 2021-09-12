from fractions import _gcd
def rut(a, b):
    gcd = _gcd(a, b)
    a = a // gcd
    b = b // gcd
    if b == 1:
        print(a)
    else:
        print("{} {}".format(a, b))

n = int(input())
for i in range(n):
    a, b = [int(i) for i in input().split()]
    rut(a, b)