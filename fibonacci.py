#educative task 1 on recursion
#fibonacci series
def fibonacci(n):
    a=0
    b=1
    #c=0
    print(a)
    print(b)
    for i in range(0,n+1):
        c=a+b
        a=b
        b=c
        print(c)
s=fibonacci(5)
#print(s)

#method 2 using recursion

def fibo(n):
    a=0
    b=1

    #print(a)
    #print(b)
    if(n<=1):
        return n
    else:
        return (fibo(n-1)+fibo(n-2))
print(fibo(4))
#j=fibo(3)
#print("hsj")
#print(j)