

# factorial using recursion

def fact(n):
    if n<=1:
        #print(n)
        return n
    else:
        #print(n)
        return n*fact(n-1)
        #print("n is now",n)

n=int(input("Enter the value of n :"))

print("Factorial is :",fact(n))