s=input()
x=[]
for i in s:
    if i not in "123456789":
        continue
    else:
        x.append(int(i))
print(sum(x))
