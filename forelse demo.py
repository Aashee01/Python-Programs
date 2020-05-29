

# for else demo

cart=[10,20,30,40,507]

for item in cart:
    if item>500:
        print("Sorry we cannot place your order thus breaking!!")
        break
    print("Your itmes are processing ",item)
else:
    print("All items are sucessfully processed")

a=None
print(a)