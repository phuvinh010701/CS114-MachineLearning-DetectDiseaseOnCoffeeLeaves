def binarySearch (arr, l, r, x):
    l=0
    r= n-k
    while l <r:
        mid =l + (r-l)//2
        if x - arr[mid] > arr[mid+k]- x:
            l = mid+1
        else:
            r=mid

    return l

n = int(input())
temp2= input()
arr= list(map(int,temp2.split()))
temp = input().split()
x = int(temp[1])
k = int(temp[0])

local = binarySearch(arr,0,0,x)

left= local
right= left+k

print(*arr[left:right])