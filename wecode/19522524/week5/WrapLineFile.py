
fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
s = fin.readline()
print(s)


# s = stdin.readline().split('  ')
# s = ' '.join(s)

# # print(s)
n = int(fin.read())
print(n)

while True:
    i = s.find(' ')
    if i == -1:
        # print(s)
        fout.write(s + "\n") 
        exit()
    if i > n:
        # print(s[:i])
        fout.write(s[:i]+ "\n")
        s = s[i + 1:]
    else:
        if len(s) <= n:
            #print(s)
            fout.write(s+ "\n")
            exit()
        while 0 < s.find(' ', i + 1) <= n and s.find(' ', i + 1) != -1:
            i = s.find(' ', i + 1)
        if i == n:
            i -= 1
        k = s[: i + 1]
        #print(s[:i + 1])
        fout.write(s[:i + 1]+ "\n")
        s = s[i + 1: ]

# fin.close()
# fout.close()