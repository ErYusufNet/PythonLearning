#Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or pounds? (K or L): ")
if unit == "K":
    weight = weight * 2.205
elif unit == "L":
    weight = weight * 2.205
else:
    print(f"{unit} is not a valid unit")
print(f"your weight is: {weight} {unit}")
