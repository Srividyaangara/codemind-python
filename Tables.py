m,n=map(int,input().split())
for i in range(1,n+1):
    p=m*i
    if i%2==0:
        continue
    print(m,'x',i,'=',p)