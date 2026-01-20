def perfect(n):
    sum=0
    for i in range(1,n):
        if (n%i==0):
            sum+=i
    return sum==n

n=int(input("Enter a num:"))
flag=perfect(n)
if flag:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")
