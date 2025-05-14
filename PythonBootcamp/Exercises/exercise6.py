unit = input("Is this temperature in Celsius or Fahrenheit (C/F) ")
temp = float(input("enter the temperature: "))
if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"the temperature in fahrenheit is {temp}")
elif unit == "F":
    temp = round((temp -32) *5 / 9, 1)
    print(f"the temperature in celsius is {temp}")
else:
    print("invalid input")
