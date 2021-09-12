def check(str1, str2):
    str1 = set(str1)
    str2 = set(str2)
    for i in str1:
        if i in str2:
            return "YES"
    return "NO"



n = int(input())

for i in range(n):
    str1 = input()
    str2 = input()
    print(check(str1, str2))
                