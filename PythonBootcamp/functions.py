'''#function a block of reusable code
#Place () after the function name to invoke it
def happy_birthay(name, age):
    print(f"Happy Birthay {name}")
    print(f"You are {age} years old.")
happy_birthay("Yusuf", 30)

def greet(name, city):
    print(f"Hello, {name}! Welcome from {city}")
    print("We hope you enjoy your stay.")
greet("Yusuf", "Helsinki")'''
#RETURN:
#Statement used to end a function and send a result back to the caller
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
first_name = input("enter first name: ")
last_name = input("enter last name: ")
full_name = create_name(first_name, last_name)
print(full_name)

