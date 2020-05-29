

# to find given substring is present or not and count the number of occourences

s=input("Enter main string:")

subs=input("Enter substring:")
flag=False
pos=-1
n=len(s)
count=0
while True:
    pos=s.find(subs,pos+1,n)
    if pos==-1:
        break
    print("Found at index:",pos)
    flag=True
    count=count+1
if flag==-1:
    print("No substring found")
print("Total occurence of substring is :",count)
