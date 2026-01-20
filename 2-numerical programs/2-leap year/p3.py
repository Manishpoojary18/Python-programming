def isleap(year):
    return (((year%100!=0) and (year%4==0)) or (year%400==0))

sr=int(input("Enter start year:"))
er=int(input("Enter end year:"))
if sr>er:
    print("invalid syntax")
else:
    print("leap years:")
    for i in range(sr,(er+1)):
        flag=isleap(i)
        if flag:
            print(i,end=" ")
    
    print("\nnon-leap years:")
    for i in range(sr,(er+1)):
        flag=isleap(i)
        if not flag:
            print(i,end=" ")





    
