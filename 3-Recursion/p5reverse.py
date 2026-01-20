def reverse(n,rev,temp):
    if n<=0:
        return rev
    
    rem=n%10
    rev=(rev*10)+rem
    n=n//10

    return reverse(n,rev,temp)

n=int(input("Enter num:"))
res=reverse(n,0,n)
print(f"reverse of {n} is {res}")