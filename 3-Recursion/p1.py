# def printnum4(n):
#     print(n)
#     printnum3(n-1)

# def printnum3(n):
#     print(n)
#     printnum2(n-1)

# def printnum2(n):
#     print(n)
#     printnum1(n-1)

# def printnum1(n):
#     print(n)

# printnum4(4)


def printnum(n):
    if n<=0:
        return
    print(n)
    printnum(n-1)

n=int(input("Enter num:"))
printnum(n)