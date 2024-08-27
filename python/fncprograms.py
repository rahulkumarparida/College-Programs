def square(sq):
    return sq*sq

def rectangle(l,b):
    return l*b

def cube(l,b,h):
    return l*b*h

def evenodd(n):
    if(n%2==0):
        return "even"
    elif(n%2!=0):
        return "odd"

print("1. Area of the Square")
print("2. Area of the Rectangle")
print("3. Volume of the Cube")
print("4. If number is Even or Odd")
ch=int(input("______MAKE A CHOICE_____ "))
if ch==1:
    print("----Area of Square----")
    sq=int(input("enter the side:- "))
    print("Area is ", square(sq))
elif ch==2:
    print("----Area of the Rectangle----")
    l=int(input("enter the length:- "))
    b=int(input("enter the breadth:- "))
    print("Area is ", rectangle(l,b))
elif ch==3: 
    print("----volume of the Cube----")
    l=int(input("enter the length:- "))
    b=int(input("enter the breadth:- "))
    h=int(input("enter the height:- "))
    print("Volume is ", cube(l,b,h))
elif ch==4:
    print("----Even or Odd----")
    n=int(input("enter the number:- "))
    print("Number is ", evenodd(n))
else:
    print("Choice not available")
