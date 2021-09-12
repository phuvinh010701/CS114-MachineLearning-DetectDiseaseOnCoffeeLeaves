a=int(input())
b=int(input())
c=int(input())
import math
if a+b>c and b+c>a and a+c>b and a>0 and b>0 and c>0 :
    P=(a+b+c)/2
    S= round(math.sqrt(P*(P-a)*(P-b)*(P-c)),2)
    if S == int(S):
        S = int(S)
    if a==b==c:
        print('Tam giac deu, dien tich =',S)
    elif (a==b) or (a==c) or (c==b):
        print('Tam giac can, dien tich = ',S)
    elif (b*b+a*a==c*c) or (a*a+c*c==b*b) or (b*b+c*c==a*a):
        print('Tam giac vuong, dien tich =',S)
    else:
        print('Tam giac thuong, dien tich =',S)
else:
    print('Khong phai tam giac')