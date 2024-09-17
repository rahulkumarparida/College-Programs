import math
#GCD of number
def gcd(a, b):
    return math.gcd(a, b)
n1= int(input("Enter a Number: "));
n2 = int(input("Enter Another Number: "))
print(f"The GCD of {n1} and {n2} is {gcd(n1, n2)}")
#power of a number
def power(a,b):
    return math.pow(a,b);
num1= int(input("Enter a Number: "));
num2 = int(input("Enter Another Number: "))
print(f"The power of {num1} and {num2} is {power(num1, num2)}")
