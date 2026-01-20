def countdigits(n):
    count=0
    while n>0:
        n=n//10
        count+=1
    return count

n=int(input("Enter num:"))
temp=n
if n<0:
    n=n*(-1)
pow=countdigits(n)
asn=0
while n>0:
    base=n%10
    asn=asn+(base**pow)
    n=n//10
if temp<0:
    asn=asn*(-1)
if temp==n:
    print(f"{n} is a armstrong number")
else:
    print(f"{n} is not an armstrong number")