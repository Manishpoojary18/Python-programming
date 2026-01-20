def ispal(n,rev,temp):
    if n<=0:
        return temp==rev
    
    rem=n%10
    rev=(rev*10)+rem
    n=n//10

    return ispal(n,rev,temp)

n=int(input("Enter num:"))
flag=ispal(n,0,n)
if flag:
    print(f"{n} is an integer palindrome")
else:
    print(f"{n} is not an intger palindrome")
