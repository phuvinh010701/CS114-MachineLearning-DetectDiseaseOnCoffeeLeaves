import sys
k = int(sys.stdin.readline())


for i in range(k):
    inp= sys.stdin.readline().split()
    s= sys.stdin.readline().split()

    u= inp[1]
    print(s.count(u))