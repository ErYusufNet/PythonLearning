#While loop = execute some code while some condition remains true

name = input("Enter your name: ")
age = int(input("Enter your age: "))
while name == "":
    print("You didn't enter a name")
    name = input("Enter your name: ")
while age  < 0:
    print("Age cannot be negative")
    age = input("Enter your age: ")


print(f"Hello {name} end = """)

