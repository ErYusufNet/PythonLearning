for i in range(1, 101):
    if i % 7 == 0 and "7" in str(i):
        print("FizzBuzz")
    elif i % 7 == 0:
        print("Fizz")
    elif "7" in str(i):
        print("Buzz")
    else:
        print(i)
