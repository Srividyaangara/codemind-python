s=input()
x=[]
for i in s:
    k=int(i)
    if k%2!=0:
        j=k*k
        x.append(j)
    else:
        continue
for i in x:
    print(i,end="")