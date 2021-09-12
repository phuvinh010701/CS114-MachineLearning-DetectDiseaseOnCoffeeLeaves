con, chan = [int(i) for i in input().split()]

# 2x + 4y = chan
# x + y = con
# x = con - y
# 2(con - y) +  4(y) = chan
# 2con +2y = chan
y = (chan - 2 * con) // 2
x = con - y
print("{} {}".format(x, y))