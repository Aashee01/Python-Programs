#educative task 1 on modules and function

#greatest common divisor
import math
def gcd(a,b):
   # a=int(input("enter number :"))
    #b=int(input("enter number :"))
    if a>b:
        small=b
    else:
        small=a
    for i in range(1,small):
        if((a%i==0) and (b%i==0)):
            gcd=i
    return gcd
c=gcd(8,12)
print(c)
print(math.gcd(8,12))