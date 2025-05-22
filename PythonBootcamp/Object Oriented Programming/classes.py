class Person():
    #property
    name = ""
    age = 0
    gender = ""

    # method initializer
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

person1 = Person("Yusuf", 27, "Male")
person2 = Person("John", 22, "Male")

class Dog():
    
    def __init__(self,age):
        self.age = age
    def humenAge(self):
        return self.age * 7

myDog = Dog(3)





