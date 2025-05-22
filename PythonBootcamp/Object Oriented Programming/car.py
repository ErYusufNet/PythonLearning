class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This car "+ self.model+" is driving")
    def stop(self):
        print("This car "+self.model+" is stopped")
    def carinfo(self):
        print(f"This is {self.make} , {self.model} is made  in {self.year} y {self.color} color car")