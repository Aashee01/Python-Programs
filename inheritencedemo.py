# car class inherited from vehicle class

class Vehicle:
    def __init__(self, maker, model, color):
        self.maker = maker
        self.model = model
        self.color = color

    def printDetails(self):
        print("Manufacturer is : ", self.maker)
        print("Model is : ", self.model)
        print("color is :", self.color)


class Car(Vehicle):
    def __int__(self, maker, model, color, door):
        Vehicle.__init__(self, maker, model, color)
        self.door = door

    def printCarDetails(self):
        self.printDetails()
        print("No of door ", self.door)


ob = Car("suzuki","23","black","7")
ob.printCarDetails()
