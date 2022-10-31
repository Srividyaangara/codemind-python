def rev(n):
    sum=0
    while n:
        d=n%10
        sum=sum*10+d
        n=n//10
    return sum 

n=int(input())
gi=rev(n)
if(rev(gi*gi)==n*n and rev(n*n)==gi*gi):
    print("True")
else:
    print("False")
