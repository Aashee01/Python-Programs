
for fizzbuzz in range(100):

    if fizzbuzz%3==0 and fizzbuzz%5==0:
        print("FizzBuzz",fizzbuzz)
    elif fizzbuzz%3==0:
        print("Fizz",fizzbuzz)
    elif fizzbuzz%5==0:
        print("Buzz",fizzbuzz)
    continue
print("FizzBuzz",fizzbuzz)
