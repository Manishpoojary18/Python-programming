def factors(n,i):
    if i>n:
        return 
    if n%i==0:
        print(i)
    return factors(n,i+1)

n=int(input("Enter num:"))
print(f"Factors of {n} are :")
factors(n,1)
