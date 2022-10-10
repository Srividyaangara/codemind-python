import math
num=int(input())
sqr=math.pow(num,2)
sum=0
while sqr>0:
    r=sqr%10
    sum=sum+r
    sqr=sqr//10
if(sum==num):
    print("Neon Number")
else:
    print("Not Neon Number")