
MOD =1000000007
n = int(input())
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    a = 0 
    b = 1 
    for i in range(2,n+1):
        c=(a+b)%MOD
        a=b
        b=c
    print(b)
