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

sr=int(input("Enter start value:"))
er=int(input("Enter end value:"))
if sr>er:
    print("invalid syntax")
else:
    print("asn's are:")
    for i in range(sr,er+1):
        flag=isasn(i)
        if flag:
            print(i,end=" ")

    print("\nnon-asn's are:")
    for i in range(sr,er+1):
        flag=isasn(i)
        if not flag:
            print(i,end=" ")
