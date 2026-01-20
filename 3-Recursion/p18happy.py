def ishappy(n):
    if n==1:
        return True
    elif n==4:
        return False
    
    sum=0
    while n>0:
        base=n%10
        sum=sum+(base**2)
        n=n//10
    return ishappy(sum)
n=int(input("Enter num:"))
flag=ishappy(n)
if flag:
    print(f"{n} is happy number")
else:
    print(f"{n} is not a happy number")