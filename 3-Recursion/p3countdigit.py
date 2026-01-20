def countdigit(n,count=0):
    if n<=0:
        return count
    n=n//10
    count=count+1
    return countdigit(n,count)

num=int(input("Enter num:"))
res=countdigit(num)
print(f"the count of digits in {num} is :{res}")
