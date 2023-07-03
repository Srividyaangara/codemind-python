s=input()
p=list(s)
x=0
y=0
for i in p:
    if i=='z':
        x+=1
    elif i=='o':
        y+=1
if x*2 == y:
    print("Yes")
else:
    print("No")