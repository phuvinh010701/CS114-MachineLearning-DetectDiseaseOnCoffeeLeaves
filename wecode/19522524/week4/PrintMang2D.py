import sys
r, c = map(int, sys.stdin.readline()[:-1].split())

arr = []
max_len = [0] * c
for i in range(r):
    k = sys.stdin.readline().split()
    for i in range(c):
        if k[i] == '-0':
            k[i] = '0'
        elif k[i][0] == '0' and k[i][-1] != 0:
            index = 0
            while k[i][index] == '0':
                index += 1
            k[i] = k[i][index:]
        max_len[i] = max(max_len[i], len(k[i]))
    arr.append(k)

for i in arr:
    for k in range(c):
        i[k] = ' ' * (max_len[k] - len(i[k])) + i[k]
        if k == c - 1:
            sys.stdout.write(i[k] + "\n")
        else:
            sys.stdout.write(i[k] + " ")