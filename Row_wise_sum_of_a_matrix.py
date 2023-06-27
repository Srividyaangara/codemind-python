n,m=map(int,input().split())
mat=[]
x=[]
for i in range(n):
    mat.append(list(map(int,input().split())))
for i in range(n):
    sumofrow=sum(mat[i])
    x.append(sumofrow)
print(*x)