n, m = [int(i) for i in input().split()]
r, c = [int(i) for i in input().split()]

inp = ''

import sys

if n * m != r * c:
    for i in range(n):
        sys.stdout.write(sys.stdin.readline())
else:
    temp = []
    id = 0
    s = []
    for i in range(n):

        l = sys.stdin.readline()[:-1].split()
        if len(s) + len(l) < c:

            s = s + l

        else:
            # print(*(s + l[:v - len(s)]))

            sys.stdout.write(" ".join(s + l[:c - len(s)]) + '\n')
            s = l[c - len(s):]
    # print(*s)
    sys.stdout.write(" ".join(s) + '\n')


    # inp = list(map(int, inp.split()))
    # #print(inp)
    # i = 0
    # j = 0
    # while i < r * c:
    #     print(inp[i], end = ' ')
    #     i += 1
    #     j += 1
    #     if j == c:
    #         print()
    #         j = 0