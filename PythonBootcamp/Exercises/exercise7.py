'''
This program checks if a user is eligible to get a driver's license.
If the user is under 18 years old, they are not eligible.
If the user is 18 or older, the program asks if they have a medical report.
A medical report is required to be eligible for a driver's license.
'''


age = int(input("Enter your age: "))

if age < 18:
    print("Sorry, you can't get a driver's license.")
else:
    medical = input("Do you have a medical report? (Y/N): ")
    if medical == "Y":
        print("You are eligible to get a driver's license.")
    else:
        print("You are older than 18 but you need to have a medical report.")
