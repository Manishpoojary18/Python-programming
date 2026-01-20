def fibo(pos):
    n1,n2=0,1
    temp=1 #no need to write temp=1,if we didn't write temp=1 also here,it will work.

    #Decrementing while loop
    # while pos>0:
    #     print(n1)
    #     temp=n1+n2
    #     n1=n2
    #     n2=temp
    #     pos-=1

    # Incrementing while loop
    # i=1
    # while i<=pos:
    #     print(n1)
    #     temp=n1+n2
    #     n1=n2
    #     n2=temp
    #     i+=1

    #Decrementing for loop
    for i in range(pos,0,-1):
        print(n1)
        temp=n1+n2
        n1=n2
        n2=temp
   
    #Incrementing for loop
    # for i in range(1,(pos+1)):
    #     print(n1)
    #     temp=n1+n2
    #     n1=n2
    #     n2=temp
pos=int(input("Enter a position:"))
fibo(pos)
