n = int(input())
import sys
from bisect import bisect_left
arr = list(map(int, sys.stdin.readline().split()))

res = []

while True:
    try:
        k, x = [int(i) for i in sys.stdin.readline().split()]
        len_arr = len(arr)
        index_find = bisect_left(arr, x, 0, len_arr - 1)
        left = max(0, index_find - k + 1)
        right = k + left - 1
        try:
            while arr[right + 1] - x < x - arr[left]:
                left += 1
                right += 1
        except:
            pass
        print(arr[left], arr[right])
    except Exception as e:
        break