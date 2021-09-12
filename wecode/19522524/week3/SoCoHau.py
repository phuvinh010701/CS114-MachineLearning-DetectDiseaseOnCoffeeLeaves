inp = input().split()
n = inp[0]
len_n = len(n)
n = int(n)
m = inp[1]
len_m = len(m)
m = int(m)

temp = 10**len_n

m = m - n
res = m // temp + 1
print(res)