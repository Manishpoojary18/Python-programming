def countdigits(n,count=0):
    if n<=0:
        return count
    n=n//10
    count+=1
    return countdigits(n,count)

def isasn(n,asn,pow,temp):
    if n<=0:
        return temp==asn
    base=n%10
    asn=asn+(base**pow)
    n=n//10
    return isasn(n,asn,pow,temp)

n=int(input("Enter num:"))
power=countdigits(n)
flag=isasn(n,0,power,n)
if flag:
    print(f"{n} is an asn")
else:
    print(f"{n} is not an asn")

