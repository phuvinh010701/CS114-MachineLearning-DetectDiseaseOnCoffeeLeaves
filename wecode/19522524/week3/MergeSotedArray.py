n = input()
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr3 = arr1 + arr2
arr3.sort()
print(*arr3)