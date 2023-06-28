n,m=map(int,input().split())
mat=[]
for i in range(n):
    il=list(map(int,input().split()))
    mat.append(il)
x=[]
for i in range(1,n-1):
    for j in range(1,m-1):
        x.append(mat[i][j])
print(sum(x))
