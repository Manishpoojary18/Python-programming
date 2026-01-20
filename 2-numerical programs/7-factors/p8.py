def factors(n):
    i=1
    countfactor=0
    countcycle=0
    while i*i<=n:
        if (n%i==0):
            print(i,end=" ")
            countfactor+=1
            if i!=(n//i):
                print(n//i,end=" ")
                countfactor+=1
        countcycle+=1
        i+=1
    return countfactor,countcycle

n=int(input("Enter a num:"))
print(f"factors of {n} are: ")
cf,cc=factors(n)
print(f"count factors of {n} are: {cf}")
print(f"count cycle of {n} are: {cc}")


    
