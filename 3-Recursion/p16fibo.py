def fiboseries(pos,n1,n2):
    if pos<=0:
        return
    print(n1,end=" ")
    fiboseries((pos-1),n2,(n1+n2))

pos=int(input("Enter pos:"))
fiboseries(pos,0,1)

