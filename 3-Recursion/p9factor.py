def factor(n,i):
    if i*i>n:
        return
    if n%i==0:
        print(i)
        if i!=(n//i):
            print(n//i)

    return factor(n,i+1)

n=int(input("Enter num:"))
print(f"factors of {n} are:")
factor(n,1)
    