n=int(input("Enter num:"))
odd=1
for i in range(1,(n+1)):
    for k in range((n*2)-1,odd,-1):
        print(" ",end="")
    for j in range(1,odd+1):
        print("* ",end="")
    print()
    odd+=2
        