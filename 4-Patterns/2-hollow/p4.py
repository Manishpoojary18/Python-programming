n=int(input("Enter num :"))
for i in range(1,(n+1)):
    for j in range(1,(n+1)):
        if (i+j)==(n+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()