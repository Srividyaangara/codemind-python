n=(input().split())
k=0
for i in range (0,int(n[0])):
    a=input().split()
    for j in range(0,int(n[1])):
        if (j!=0 and j!=int(n[1])-1 and i!=0 and i!=int(n[0])-1):
            k=k+int(a[j])
print (k)           