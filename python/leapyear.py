x=int(input("Enter the year:--"))
if x%4==0:
    if x%100==0:
        if x%400==0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("leap year")
else:
    print("Not a leap year")
