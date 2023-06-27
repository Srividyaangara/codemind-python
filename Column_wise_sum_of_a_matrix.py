n,m=map(int,input().split())
mat=[]
for i in range(n):
    mat.append(list(map(int,input().split())))
x=[]
for i in range(m):
    s=0
    for j in range(n):
        s=s+mat[j][i]
    x.append(s)

print(*x)