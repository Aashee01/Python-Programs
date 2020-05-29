# check condition befor printing fibonacci sereies

def fib(n):
    if n<0:
        print("invalid number")
        return -1
    else:
        a=0
        b=1
        print(a)
        print(b)
        if n==1:
            print(a)
        else:
            for i in range(2,n):
                c=a+b
                a=b
                b=c
                if c>n:
                    break
                print(c)
fib(100)