# find grade of students based on marks

sub1=int(input("enter marks in subject 1"))

sub2=int(input("enter marks in subject 2"))

sub3=int(input("enter marks in subject 3"))

sub4=int(input("enter marks in subject 4"))

sub5=int(input("enter marks in subject 5"))

avg=sub1+sub2+sub3+sub4+sub5/5

print("average of student in 5 subject :",avg)
if(avg>90):
    print("Grade A")
elif(avg>80 and avg<90):
    print("grade B")
elif(avg>70 and avg<80):
    print("Gracde C")
elif(avg>60 and avg<70):
    print("Grade D")
else:
    print("fail")