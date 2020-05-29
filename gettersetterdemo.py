# demo of getter and setter method

class User:
    def __init__(self,username):
        self.__username=username
    def setUsername(self,x):
        self.__username=x
    def getUsername(self):
        return (self.__username)
ob=User('steve')
print("before setting user name : "+ob.getUsername())
ob.setUsername('Mark')
print("after setting user name : "+ob.getUsername())