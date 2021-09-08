def fibo(n):
    a = [1] * n

    for i in range(2, n):
        a[i] = a[i - 1] + a[i - 2]
    return a[n - 1]

def solve(n):
    if 1 <= n <= 30:
        print(fibo(n))
    else:
        print("So {} khong nam trong khoang [1,30].".format(n))

solve(int(input()))