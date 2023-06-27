r,c=map(int,input().split())
m=[]
for i in range(r):
    il=list(map(int,input().split()))
    m.append(il)

x=[]
y=[]
for i in range(r):
    for j in range(c):
        if i==0 or j==0 or i==r-1 or j==r-1:
            x.append(m[i][j])
        else:
            y.append(m[i][j])
s=sum(x)
print(s)