def factors(n):
    countfactor=0
    countcycle=0
    for i in range(1,(n+1)):
        if (n%i==0):
            print(i,end=" ")
            countfactor+=1
        countcycle+=1
    return countfactor,countcycle

n=int(input("Enter num:"))
print(f"factors of {n} are:")
cf,cc=factors(n)
print(f"\ncount factor of {n} is : {cf}")
print(f"count cycle of {n} is : {cc}")