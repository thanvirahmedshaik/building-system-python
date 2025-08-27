# Billing System in Python

def display_menu():
    print("\n===== WELCOME TO BILLING SYSTEM =====")
    print("1. Pizza - ₹150")
    print("2. Burger - ₹80")
    print("3. Sandwich - ₹50")
    print("4. Coke - ₹40")
    print("5. Exit")
    print("=====================================")


# Menu items with prices
menu = {
    1: ("Pizza", 150),
    2: ("Burger", 80),
    3: ("Sandwich", 50),
    4: ("Coke", 40)
}

bill = []
total = 0

while True:
    display_menu()
    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        break

    if choice in menu:
        qty = int(input(f"Enter quantity of {menu[choice][0]}: "))
        price = menu[choice][1] * qty
        bill.append((menu[choice][0], qty, price))
        total += price
        print(f"{menu[choice][0]} x {qty} added to bill. Subtotal: ₹{total}")
    else:
        print("Invalid choice! Please try again.")

# Final Bill
print("\n========== FINAL BILL ==========")
print("{:<10} {:<10} {:<10}".format("Item", "Qty", "Price"))
for item, qty, price in bill:
    print("{:<10} {:<10} ₹{:<10}".format(item, qty, price))
print("-------------------------------")
print(f"TOTAL AMOUNT: ₹{total}")
print("================================")
print("Thank you! Visit Again 🙏")
