import mymodules
from mymodules import calculateTwo;
from mymodules import calculateSquare;

s = int(input("Enter a number : "));
ar =  mymodules.calculateSquare;
calc = mymodules.calculateTwo;

print("Area of the sqaure is : ");
are = ar.area(s);
print(are);

print("Permiter of the square is : ")
peri =ar.perimeter(s);
print(peri);

print("Volume of the Cube is : ");
vol = ar.volume(s);
print(vol);


a = int(input("Enter first number : "));
b = int(input("Enter second number : "));

print("Addition of two numbers is : ");
ad = calc.add(a,b);
print(ad);

print("Substraction of two numbers is : ");
sub =calc.substract(a,b);
print(sub)

print("Divisioin of two numbers is : ");
div = calc.divide(a,b);
print(div)

print("Multiplacation of two numbers is : ");
mul = calc.multiply(a,b);
print(mul)

print("Modulus of two numbers is : ");
mod = calc.modulo(a,b);
print(mod);

#OUTPUT
#Enter a number : 5
#Area of the sqaure is : 
#25
#Permiter of the square is : 
#20
#Volume of the Cube is : 
#125
#Enter first number : 10
#Enter second number : 15
#Addition of two numbers is : 
#25
#Substraction of two numbers is : 
#-5
#Divisioin of two numbers is : 
#0.6666666666666666
#Multiplacation of two numbers is : 
#150
#Modulus of two numbers is : 
#10
