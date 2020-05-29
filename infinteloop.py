
# Example of infinte loop

n=10
# since we does not put any condition inside the loop this goes infinte
while True:
    print(n , end=' ')
    n=n-1
    print("done!")
    # this above will undergo an infinite loop
    # to stop infinte loop we use break
    break