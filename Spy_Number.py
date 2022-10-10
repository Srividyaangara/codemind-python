def spy(n):
    sum=0
    mul=1
    while n:
        r=n%10
        sum=sum+r
        mul=mul*r
        n=n//10
    if(sum==mul):
        return "Spy Number"
    else:
        return "Not Spy Number"

n=int(input())
print(spy(n))