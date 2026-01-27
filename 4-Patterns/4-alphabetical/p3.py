n=int(input("Enter num:"))
for i in range(n,1-1,-1):
    for j in range(1,i+1):
        if i%2==0:
            print(chr(64+j),end="")
        else:
            print(chr(96+j),end="")
    print()