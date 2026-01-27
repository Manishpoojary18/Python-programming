n=int(input("Enter num:"))
for i in range(1,(n+1)):
    for j in range(n,i-1,-1):
        print(chr(96+j),end="")
    print()