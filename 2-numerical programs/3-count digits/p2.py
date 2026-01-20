def countdigits(n):
    count=0
    while n>0:
        n=n//10
        count+=1
    return count

n=int(input("enter a number:"))
res=countdigits(n)
print(f"The number of digits in {n} is:{res}")