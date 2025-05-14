#While loop = execute some code while some condition remains true

name = input("Enter your name: ")
while name == "":
    print("You didn't enter a name")
    name = input("Enter your name: ")

print(f"Hello {name}")
