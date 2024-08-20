x=int(input("Enter 1st:--"))
y=int(input("Enter 2nd:--"))
z=int(input("Enter 3rd:--"))
g=x if x>y and x>z else y if y>z else z
print("the greatest is ",g)
