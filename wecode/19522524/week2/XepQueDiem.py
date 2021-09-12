n = int(input())

def check(i):
    if i == 2:
        return 2
    if i % 2 != 0:
        return 1
    else:
        return 0

for i in range(n):
    k = int(input())
    print(check(k))