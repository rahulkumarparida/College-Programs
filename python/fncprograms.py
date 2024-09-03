<<<<<<< HEAD

=======
>>>>>>> 1d6965cd457d19169938f9ec704f00169433e155
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
<<<<<<< HEAD
def prime(n):
	n=int(input("Enter number to check: "))
	f=0
	i=2
	while (i<=(n//2)):
    		if((n%i)==0):
        	f = 1
        	break
    		i+=1
		if(n==1):
    			return "1 is neither prime nor composite"
		elif(f==0):
    			return " a prime number."
		else:
    			return " a composite number."
=======
>>>>>>> 1d6965cd457d19169938f9ec704f00169433e155

print("1. Area of the Square")
print("2. Area of the Rectangle")
print("3. Volume of the Cube")
print("4. If number is Even or Odd")
<<<<<<< HEAD
print("5. Prime or not")
=======
>>>>>>> 1d6965cd457d19169938f9ec704f00169433e155
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
<<<<<<< HEAD
elif ch==5:
	
    print("----Prime or Composite----")
    n=int(input("enter the number:- "))
    print(prime(n))
=======
>>>>>>> 1d6965cd457d19169938f9ec704f00169433e155
else:
    print("Choice not available")
