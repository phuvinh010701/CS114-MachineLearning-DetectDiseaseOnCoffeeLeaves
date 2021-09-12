k, t = [int(i) for i in input().split()]

if (t//k)%2==0:
    print(t % k)
else:
    print(k - (t%k))