def fibo(pos):
    if pos==1 or pos==0:
        return pos
    return fibo(pos-1)+fibo(pos-2)

pos=int(input("Enter pos:"))
res=fibo(pos)
print(res)