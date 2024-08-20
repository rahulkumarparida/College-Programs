n=int(input("Enter number to check: "))
f=0
i=2
while (i<=(n//2)):
    if((n%i)==0):
        f = 1
        break
    i+=1
if(n==1):
    print("1 is neither prime nor composite")
elif(f==0):
    print(n,"is a prime number.")
else:
    print(n,"is a composite number.")
