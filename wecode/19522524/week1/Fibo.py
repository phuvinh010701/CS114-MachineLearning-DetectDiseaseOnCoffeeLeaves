def solve():
    n = int(input())
    if 1 <= n <= 30:
        f = [1] * 31
        for i in range(2, 31):
            f[i] = f[i - 1] + f[i - 2]
        print(f[n - 1])
    else:
        print("So {} khong nam trong khoang [1,30].".format(n))

solve()