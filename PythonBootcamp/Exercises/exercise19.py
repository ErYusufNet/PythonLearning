# shop

menu = {
    "pizza": 3.00,
    "popcorn": 6.00,
    "cola": 3.30
}
cart = []
total = 0

print("---------- MENU ----------")
for key, value in menu.items():
    print(f"{key:10}: €{value:.2f}")
print("--------------- ----------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("Item not found in the menu.")

print("---------- YOUR ORDER ----------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print(f"Total: €{total:.2f}")
