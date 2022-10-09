def fun(n):
    a=n
    while(n>0):
        r=n%10
        if(a%r!=0):
            return 0
        n//=10
    return 1
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(i%10==0):
        continue
    if(fun(i)):
        print(i,end=" ")