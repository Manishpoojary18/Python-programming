def countdigits(n):
    count=0
    while n>0:
        n=n//10
        count+=1
    return count
def isasn(n):
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
    return temp==asn

num=int(input("Enter num:"))
series=1
print(f"first {num} natural Non-arm strong numbers are:")
while num>0:
    flag=isasn(series)
    if not flag:
        print(series)
        num=num-1
    series=series+1