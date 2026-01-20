def intpalindrome(n):
    temp=n
    if n<0:
        n=n*(-1)
    rev=0
    while n>0:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    if temp<0:
        rev=rev*(-1)
    return temp==rev

n=int(input("Enter a num:"))
flag=intpalindrome(n)
if flag:
    print(f"{n} is a integer palindrome")
else:
    print(f"{n} is not an integer palindrome")
