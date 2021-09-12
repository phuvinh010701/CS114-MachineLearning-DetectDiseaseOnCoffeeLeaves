n = int(input())
from math import ceil
for i in range(n):
    k = int(input())
    arr = list(map(int, input().split()))

    sum_arr = sum(arr)
    print(ceil(sum_arr / k))
