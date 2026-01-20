num=int(input("Enter a number:"))
if num>0:
    if num%3==0 and num%5==0:
        print("fizz buzz number")
    elif num%3==0:
        print("fizz number")
    elif num%5==0:
        print("buzz number")
    else:
        print("you have entered a number")
else:
    print("Neutral")