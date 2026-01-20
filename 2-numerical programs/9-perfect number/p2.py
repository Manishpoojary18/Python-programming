def isperfect(n):
    i=1
    sum=0
    while i*i<n:
        if n%i==0:
            sum=sum+i
            if i!=n//i and n!=n//i:
                sum=sum+(n//i)
        i+=1
    return sum==n
n=int(input("Enter num:"))
flag=isperfect(n)
if flag:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")