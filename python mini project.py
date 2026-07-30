# ========== CAFE BILLING SYSTEM ==========

menu = {
    "Burger": 250,
    "Pizza": 500,
    "Sandwich": 180,
    "Coffee": 120,
    "Tea": 60,
    "Cold Drink": 80,
    "French Fries": 150
}

total_bill = 0

print("=" * 40)
print("      WELCOME TO Alif's CAFE")
print("=" * 40)

print("\n------ MENU ------")
for item, price in menu.items():
    print(f"{item:<20} Tk {price}")

print("-" * 40)

while True:

    item = input("\nEnter item name: ")

    if item in menu:

        quantity = int(input("Enter quantity: "))

        price = menu[item] * quantity

        total_bill += price

        print(f"{item} x {quantity} = Tk {price}")

    else:
        print("Sorry! Item not available.")

    more = input("\nDo you want to order more? (yes/no): ").lower()

    if more != "yes":
        break


print("\n" + "=" * 40)
print("           FINAL BILL")
print("=" * 40)

print(f"Total Bill : Tk {total_bill}")

print("\nThank You for Visiting Alif's Cafe!")
print("=" * 40)