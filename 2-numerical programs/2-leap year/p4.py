def isleap(year):
    return (((year%100!=0) and (year%4==0)) or (year%400==0))
sr=int(input("Enter start year:"))
er=int(input("Enter end year:"))
if sr>er:
    print("invalid syntax")
else:
    for i in range(sr,(er+1)):
        flag=isleap(i)
        if flag:
            print(f"{i} is a leap year")
        else:
            print(f"{i} is a non leap year")