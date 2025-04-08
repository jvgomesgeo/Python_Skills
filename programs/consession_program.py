#concession stand program
menu = {"pizza" : 3.00,
        "nachos": 4.5,
        "popcorn": 6.00,
        "fries" : 2.50,
        "chips" : 3.50,
        "pretzel" : 3.5,
        "soda" : 3.00,
        "lemonade" : 4.25}

cart = []
total = 0

print("-" * 5, "MENU", "-" * 5)
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

while True:
    food = input("Select an item (q to quit):").lower()
    if food == "q".lower():
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print(f"Food not in menu")

 
print("-" * 5, "YOUR ORDER", "-" * 5)
print(cart)

for food in cart:
    total += menu.get(food)
    print(food, end = " ")
print(f"The total value is: ${total:.2f}")
#dictionary {key:value}

