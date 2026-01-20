def chckgcd(n1,n2,i,hcf,lower):
    if i>lower:
        return hcf
    if n1%i==0 and n2%i==0:
        hcf=i
    return chckgcd(n1,n2,i+1,hcf,lower)
num1=int(input("Enter first num:"))
num2=int(input("Enter second num:"))
lower=num1
if num2<num1:
    lower=num2
res=chckgcd(num1,num2,2,1,)