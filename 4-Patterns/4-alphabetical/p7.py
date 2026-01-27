n=int(input("Enter num:"))
for i in range(1,(n+1)):
    count=n
    for j in range(1,(n+1)):
        if i%2!=0:
            print(chr(64+j),end="")
        else:
            print(chr(96+count),end="")
            count-=1
    print()