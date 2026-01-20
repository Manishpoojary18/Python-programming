def gcd(n1,n2):
    lower=n1
    if n2<n1:
        lower=n2
    hcf=1
    i=2
    while i<=lower:
        if n1%i==0 and n2%i==0:
            hcf=i
        i+=1
    return hcf
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
res=gcd(n1,n2)
print(f"HCF/GCD of {n1} and {n2} is : {res}")