sohocsinh=int(input())
sode=int(input())
A_sohang=int(input())
A_vitri=int(input())
if (sode%2==0):
    B_vitri=A_vitri
else:
    if (A_vitri==1):
         B_vitri=2
    elif(A_vitri==2):
        B_vitri=1
B_hang=(A_sohang-1) * 2 + (A_vitri-1)
if B_hang-sode>=0:
    print((B_hang-sode)//2+1,B_vitri)
elif B_hang+sode<=sohocsinh-1:
    print((B_hang+sode)//2+1,B_vitri)
else:
    print(-1)