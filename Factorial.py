def factorial(n):
    return 1 if (n==1 or n==0) else n*factorial(n-1);
num=int(input("Enter number :"))
print("Factorial is :",+factorial(num))

# educative factorial recursion

def factorial(n):
    if(n<=1):
        return 1
    else:
        return (n*factorial(n-1))
print("Factorial is :")
print(factorial(4))