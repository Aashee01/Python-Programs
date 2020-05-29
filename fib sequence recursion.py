

# fibonacci sequence using recursion

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)



n=int(input("Enter the number of terms :"))
#s=fib(5)

if n<0:
    print("Enter positive number :")
else:
    for i in range(n):
        print(fib(i))