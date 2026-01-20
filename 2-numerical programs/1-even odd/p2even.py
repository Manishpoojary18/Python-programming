# def evenodd(num):
#     if num%2==0:
#         return True
#     else:
#         return False
# n=int(input("Enter num:"))
# flag=evenodd(n)
# if flag:
#     print(f"{n} is even")
# else:
#     print(f"{n} is odd")



def evenodd(num):
    return num%2==0
n=int(input("Enter num:"))
flag=evenodd(n)
if flag:
    print(f"{n} is even")
else:
    print(f"{n} is odd")