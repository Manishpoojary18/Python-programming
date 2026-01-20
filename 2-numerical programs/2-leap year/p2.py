def isleap(year):
    return (((year%100!=0) and (year%4==0)) or (year%400==0))
year=int(input("Enter year:"))
flag=isleap(year)
if flag:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
