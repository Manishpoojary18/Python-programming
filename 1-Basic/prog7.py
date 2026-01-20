print("for with range():")
l1=[1,2,3]
for i in range(0,3):
    print("index:",i,"elem:",l1[i])

print("---------------------------")

print("for  without range():")
l1=[1,2,3]
for i in l1:
    print("index:",l1.index(i),"elem:",i)