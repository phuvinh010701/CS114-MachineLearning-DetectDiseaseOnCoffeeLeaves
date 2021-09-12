n = input()
leng = len(n)

sum = 0
for i in range(leng):
    sum += int(n[i]) ** leng

print(sum == int(n))