def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input("Enter the number of terms:- "))
i=0
while(i<n):
    print(fibo(i))
    i+=1
# Output for 10 dgts :- 0 1 1 2 3 5 8 13 21 34
