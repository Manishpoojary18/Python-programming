def countdigits(n):
    count=0
    while n>0:
        n=n//10
        count+=1
    return count

sr=int(input("Enter start value:"))
er=int(input("Enter end value:"))

if sr>er:
    print("Invalid input")
else:
    for i in range(sr,(er+1)):
        res=countdigits(i)
        print(f"{i} has {res} digits")
