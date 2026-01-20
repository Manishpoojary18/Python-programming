def countfactors(n):
    countfactor=0
    countcycle=0
    for i in range(1,(n+1)):
        # countcycle+=1
        if n%i==0:
            countfactor+=1
        countcycle+=1
    return countfactor,countcycle

n=int(input("Enter a num:"))
cf,cc=countfactors(n)
print(f"count factor of {n} is : {cf}")
print(f"count cycle of {n} is : {cc}")
        