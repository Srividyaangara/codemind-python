n=int(input())
l=list(map(int,input().split()))
p=sum(l)

while n:
    if p%n==0:
        print(n)
        break
    n=n-1