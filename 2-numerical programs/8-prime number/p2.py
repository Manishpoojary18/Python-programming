def isprime(n):
    i=1
    countfactor=0
    while i*i<=n:
        if (n%i==0):
            countfactor+=1
            if i!=n//i:
                countfactor+=1
        i+=1
    return countfactor==2

n=int(input("Enter a number:"))
flag=isprime(n)
if flag:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")

