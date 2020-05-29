

a=int(input("enter number :"))



try:
     for i in range(int(input())):
         a,b=input("enter other").split(" ")
     print(a//b)

except ZeroDivisionError as e:
    print("Error code:integer division or modulo division by zero")
except ValueError as e:
    print("Error code :invalid literal for int() with base 10:",e)

