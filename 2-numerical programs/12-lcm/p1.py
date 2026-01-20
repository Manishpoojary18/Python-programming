def lcm(n1,n2):
    lcm=n1
    if n1<n2:
        lcm=n2
    while True:
        if lcm%n1==0  and lcm%n2==0:
            return lcm
        lcm+=1

n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
res=lcm(n1,n2)
print(f"LCM of {n1} and {n2} is : {res}")