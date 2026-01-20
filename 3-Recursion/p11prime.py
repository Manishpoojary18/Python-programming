def isprime(n,i,countfactor):
    if i>n:
        return countfactor==2
    if n%i==0:
        countfactor+=1
    return isprime(n,i+1,countfactor)

n=int(input("Enter num:"))
flag=isprime(n,1,0)
if flag:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")