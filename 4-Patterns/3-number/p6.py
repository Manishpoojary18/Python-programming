n=int(input("Enter num:"))
for i in range(n,0,-1): 
# for i in range(n,1-1,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()