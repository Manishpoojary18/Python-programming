n=int(input("Enter num:"))
for i in range(n,1-1,-1):
    for j in range(i,1-1,-1):
        print(chr(64+j),end="")
    print()