def countfactor(n,i,countfact):
    if i*i>n:
        return countfact
    if n%i==0:
        countfact+=1
        if i!=(n//i):
            countfact+=1

    return countfactor(n,i+1,countfact)

n=int(input("Enter num:"))
res=countfactor(n,1,0)
print(f"count factor of {n} is : {res}")    