def printnum(n,i):
    if i>n:
        return
    print(i)
    printnum(n,i+1)

printnum(4,1)