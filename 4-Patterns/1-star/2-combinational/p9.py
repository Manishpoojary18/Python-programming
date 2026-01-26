n=int(input("Enter num:"))
noc=(n*2)-1
for i in range(1,(n*2)):
    for k in range((n*2)-1,noc,-1):
        print(" ",end="")
    for j in range(1,(noc+1)):
        print("*",end="")
    print()
    if i<n:
        noc-=2
    else:
        noc+=2