from sys import stdin

s = stdin.readline().strip()
n = int(input())
# k = ""
while True:
    i = s.find(' ')
    if i == -1:
        print(s)
        exit()
    if i > n:
        # k = s[: i + 1]
        print(s[:i])
        s = s[i + 1:]
    else:
        if len(s) <= n:
            # k = s
            print(s)
            exit()
        while 0 < s.find(' ', i + 1) <= n and s.find(' ', i + 1) != -1:
            i = s.find(' ', i + 1)
        if i == n:
            i -= 1
        # k = s[: i + 1]
        print(s[:i + 1])
        s = s[i + 1: ]