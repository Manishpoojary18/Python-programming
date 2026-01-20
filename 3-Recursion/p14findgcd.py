def findgcd(n1,n2):
    if n1==0:
        return n2
    if n1<n2:
        n1,n2=n2,n1
    return findgcd((n1%n2),n2)

num1=int(input("Enter first num:"))
num2=int(input("Enter second num:"))
res=findgcd(num1,num2)
print(res)

    
