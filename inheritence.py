#inheritence demo

class A:
    def feature1(self):
        print("feature 1 is working ")

    def feature2(self):
        print("fetaure 2 is working")


class B(A):
    def feature3(self):
        print("feature 3 is working")

    def feature4(self):
        print("feature 4 is working")


a=A()
print("feature of class A")
a.feature1()
a.feature2()
b=B()
print("feature of inherited class b")
b.feature3()
b.feature4()
b.feature1()
b.feature2()

print("demo of mutilevel inheritence ")

class C(B):
    def feature5(self):
        print("feature 5 is working")


c1=C()
print("now class C will inherit all feature of class A as well as class B")

print("Class C")
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()

