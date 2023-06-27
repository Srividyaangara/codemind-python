n,m=map(int,input().split())
mat=[]
x=[]
y=[]

for i in range(n):
    il=list(map(int,input().split()))
    mat.append(il)
    
    
    
for i in range(n):
    for j in range(m):
        if mat[i][j]%2==0:
            x.append(mat[i][j])
        else:
            y.append(mat[i][j])
s=sum(x)
p=sum(y)
print(s,p)
