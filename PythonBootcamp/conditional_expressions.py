#conditional expression
'''
a one-line shortcut fort the if-else statement(ternary operator)
print or assign one of two values based on condition
x if condition else Y
'''
'''
num = int(input("Enter a number: "))
print("Positive" if num > 0 else "negative")
num2 = int(input("Enter a number: "))
result = "Even" if num2 % 2 == 0 else "Odd"
print(result) '''

'''
num = 5
a = 6
b = 7
max_num = a if a > b else b
print(max_num) '''
'''
age = int(input("Enter your age: "))
status = "adulf" if age >= 18 else "baby"
print(status)'''

temp = int(input("what is the temperature? "))
weather = "hot" if temp >15 else "cold"
print(weather)


