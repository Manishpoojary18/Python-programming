def countfactors(n):
    countfactor=0
    for i in range(1,(n+1)):
        if (n%i==0):
            countfactor+=1
    return countfactor

n=int(input("Enter a num:"))
res=countfactors(n)
print(f"count factor of {n} is : {res}")