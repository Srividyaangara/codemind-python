l=int(input())
for i in range(l):
    m,n=map(int,input().split())
    x=input()
    while n:
        s=x[0:n]
        p=s[::-1]
        x=p+x[n:]
        n=n-1
    print(x)
    
    
    
    
x