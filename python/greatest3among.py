x=int(input("Enter 1st Number:--"))
y=int(input("Enter 2nd Number:--"))
z=int(input("Enter 3rd Number:--"))
if(x>y):
    if(x>z):
        print(x,"is the greatest number")
    else:
        print(z,"is the greatest number")
else:
    if(y>z):
        print(y,"is the greatest number")
    else:
        print(z,"is the geatest number")
