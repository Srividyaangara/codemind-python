r,c=map(int,input().split())
m=[]
for i in range(r):
    il=list(map(int,input().split()))
    m.append(il)
x=[]
for i in range(r):
    s=sum(m[i])
    x.append(s)
print(max(x))