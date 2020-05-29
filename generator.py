
#generator

def topten():


    yield 1
    yield 2
    yield 3


value=topten()
#this print will return an object of generator

print(value)

#to fecth value from iterator we use next()

print(value.__next__())
print(value.__next__())