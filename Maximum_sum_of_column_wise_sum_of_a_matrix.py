r,c=map(int,input().split())
m=[]
for i in range(r):
    il=list(map(int,input().split()))
    m.append(il)
x=[]
for i in range(c):
    s=0
    for j in range(r):
        s=s+m[j][i]
    x.append(s)
print(max(x))