def cal(inp, arr):
    x = inp[0]
    if x == 0:
        arr.insert(0, inp[-1])
        return True

    if x == 1:
        arr.append(inp[-1])
        return True

    if x == 2:
        if inp[1] in arr:
            arr.insert(arr.index(inp[1]) + 1, inp[-1])

        else:
            arr.insert(0, inp[-1])
        return True

    if x == 3:
        if inp[-1] in arr:
            arr.remove(inp[-1])
        return True

    if x == 4:

        while inp[-1] in arr:
            arr.remove(inp[-1])
        return True

    if x == 5:
        if len(arr) != 0:
            arr.pop(0)
        return True

    if x == 6:
        if len(arr) == 0:
            print('blank')
            return False

        for x in arr:
            print(x, end=' ')
        return False

c = True
ans = []

import sys
while c:
    k=sys.stdin.readline()
    inp = list(map(int, k[:len(k)-1].split()))
    c = cal(inp, ans)