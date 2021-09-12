import sys

def func():
    mydict = {}
    while True:
        inp = sys.stdin.readline()
        k = list(map(int, inp[:-1].split()))
        if len(k) <= 0:
            break
        check = k[0]
        if check == 0:
            break
        elif check == 1:
            mydict[k[1]] = '1\n'
        elif check == 2:
            sys.stdout.write(mydict.get(k[1], '0\n'))
        elif check == 3:
            mydict.pop(k[1], None)

func()