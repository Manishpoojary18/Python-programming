def countfact(n,i,countfactor):
    if i>n:
        return countfactor
    if n%i==0:
        countfactor+=1

    return countfact(n,i+1,countfactor)

n=int(input("Enter num:"))
res=countfact(n,1,0)
print(f"count factor of {n} is : {res}")    