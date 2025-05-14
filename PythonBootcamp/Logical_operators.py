#Logical operators = evaluate multiple conditions(or,and,not
#or = at least one condition must be true
#and = both conditions must be true
#not=inverts the condition (not false,not true)
#if its warmer than 35 and colder than 0 or if its raining then cancel the outdoor event
temp = int(input("How is the weather today? "))
is_raining = False
if temp >35 or temp < 0 or is_raining:
    print("the outdoor event is cancelled")
