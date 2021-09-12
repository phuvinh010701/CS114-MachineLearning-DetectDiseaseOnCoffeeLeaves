inp = input().split()
male = ['lios', 'etr', 'initis']
female = ['liala', 'etra', 'inites']

def check_sex(first_item):
    for i in male:
        if i in first_item:
            return True
    for i in female:
        if i in first_item:
            return False
    return -1
    
def check_true(count , arr, sex):
    flag = -1
    i = 0
    while i < len(arr):
        if sex[0] in arr[i] and flag <= 0:
            flag = 0
            i += 1
        elif sex[1] in arr[i] and flag <= 1:
            flag = 1
            i += 1
            count += 1
            if count > 1:
                return "NO"
        elif sex[2] in arr[i] and flag <= 2 and count == 1:
            flag = 2
            i += 1
        else:
            return "NO"
    return "YES"

flag_sex = check_sex(inp[0])

if flag_sex == -1:
    print("NO")
else:
    if male[1] in inp[0] or female[1] in inp[0]:
        count = 1
    else:
        count = 0
    if flag_sex == True:
        print(check_true(count, inp[1:], male))
    else:
        print(check_true(count, inp[1:], female))
