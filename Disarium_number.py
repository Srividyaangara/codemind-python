n=int(input())
t=n
s=0
while n:
    r=n%10
    s=s*10+r
    n//=10
v=s
p=0
cnt=0
while v:
    d=v%10
    if d>0:
        cnt+=1
    p=p+d**cnt
    v//=10
if (p==t):
    print("True")
else:
    print("False")