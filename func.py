

def person(name,age=90):
    print("name is :",name)
    print("age is :",age)

#position agrument
person(20,'navin')
#keyword agument becz we use variable as arguments
person(age=20,name='navin')
#default agrument
print('navin') # by defaullt age is set to 90

# variable arguments
def sum(a,*b):
   # c=a+b
     print(a)
     print(b)
     c=a
     for i in b:
         c=c+i
     print(c)
sum(4,5,4,3,2)