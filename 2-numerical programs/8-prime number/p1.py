def isprime(n):
    countfactor=0
    for i in range(1,(n+1)):
        if (n%i==0):
            countfactor+=1
    return (countfactor==2)

n=int(input("Enter a num:"))
flag=isprime(n)
if flag:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")





    