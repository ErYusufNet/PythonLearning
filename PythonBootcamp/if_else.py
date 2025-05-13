
#if =? do some code only if some condition is true
#else do something else
age = int(input("Enter your age: "))
if age >= 18 and age <30:
    print("You can get an credit card")
elif age < 10:
    print("You are child yet")
elif age >=30:
    print("You probably have an bank card already")
else:
    print("You can not get an credit card")



