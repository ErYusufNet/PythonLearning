#Cafe ordering system
drinks = []
prices = []
total = 0
while True:
    drink = input("Enter a drink(q to quit): ")
    if drink.lower() == "q":
        break
    else:
        drinks.append(drink)
        price = float(input("enter price: "))
        prices.append(price)
        total += price
print("\n----Your Order----")
for drink in drinks:
    print(drink)
print(f"Total price: €{total:.2f}")



