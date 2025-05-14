#While loop = execute some code while some condition remains true
'''
name = input("Enter your name: ")
age = int(input("Enter your age: "))
while name == "":
    print("You didn't enter a name")
    name = input("Enter your name: ")
while age  < 0:
    print("Age cannot be negative")
    age = input("Enter your age: ")


print(f"Hello {name}", end = "")
print(f"Hello {age} ")

food = input("Enter a food you like (q to quit): ")
while not food == "q":
    print(f"you like {food} ")
    food = input("Enter another food you like (q to quit): ")
print("bye") '''

num = int(input("enter a number between 1-10: "))
while num < 1 or num > 10:

    print(f"{num} is not valid")
    num = int(input("enter a number between 1-10: "))
print(f"your number is{num}")


