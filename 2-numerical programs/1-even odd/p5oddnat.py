def checkevenodd(num):
    return num%2==0
count=int(input("Enter num:"))
series=1
while count>0:
    flag=checkevenodd(series)
    if not flag:
        print(series,end=" ")
        count-=1
    series+=1