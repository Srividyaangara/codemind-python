n=int(input())
mat1,mat2,mattot=[],[],[]
for i in range(n):
    mat1.append(list(map(int,input().split())))
for i in range(n):
    mat2.append(list(map(int,input().split())))
for i in range(n):
    l=[]
    for j in range(n):
        l.append(abs(mat1[i][j]+mat2[i][j]))
    mattot.append(l)
for i in range(n):
    for j in range(n):
        print(mattot[i][j],end=' ')
    print()