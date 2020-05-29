# we can even use else with for
#print the  number from list which is divisible by 5

list=[12,2,3,46,7,107]

for i in list:
    if i%5==0:
        print(i)
        break
else:
     print("Not Found")