
# print identity matrix

row=int(input("Enter number of rows:"))

for i in range(1,row+1):
    for j in range(1,row+1):
        if i==j:

         print(1,end='',sep=" ")
        else:
            print(0,end='',sep=" ")
    print()