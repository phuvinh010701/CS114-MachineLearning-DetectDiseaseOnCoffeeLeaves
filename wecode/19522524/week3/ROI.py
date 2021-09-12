h, w = [int(i) for i in input().split()]
matrix = []

for i in range(h):
    matrix.append(input().split())

top, left, bottom, right = [int(i) for i in input().split()]

for i in range(0, top):
    print('0 '* w)

for i in range(top, bottom + 1):
    sl = '0 ' * left
    sr = ' 0' * (w - right - 1)
    src = matrix[i][left:right + 1]
    print(sl, end = '')
    print(*src, end = '')
    print(sr)

    # print(sr, step='')
    # print(sl, sep='')
    # print(*src)
    # print(sr, sep = '')
    # print()
    # print(sl, *src, sr, sep = '')

for i in range(bottom + 1, h):
    print('0 '* w)