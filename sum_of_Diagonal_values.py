r,c=map(int,input().split())
m=[]
for i in range(r):
    il=list(map(int,input().split()))
    m.append(il)
x=[]
for i in range(r):
    for j in range(c):
        if i==j or i+j==c-1:
            x.append(m[i][j])
print(sum(x))