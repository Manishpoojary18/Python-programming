def evenodd(num):
    return num%2==0
sr=int(input("Enter start value:"))
er=int(input("Enter end value:"))
if sr>er:
    print("invalid syntax")
else:
    print("Even numbers:")
    for i in range(sr,(er+1)):
        flag=evenodd(i)
        if flag:
            print(i,end=" ")
    
    print("\nodd numbers:")
    for i in range(sr,(er+1)):
        flag=evenodd(i)
        if not flag:
            print(i,end=" ")
