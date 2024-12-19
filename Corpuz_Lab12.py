'''
1. Problem Statement:
Create a Python program to simulate a simple food ordering system. 

2. Functional Requirements:
    [/] Display Menu: Present a list of food items with their prices.
    [/] Order Selection: Allow the user to choose an item from the menu. 
    [/] Calculate Total: Determine the total cost of the selected item.
    [/] Payment Processing: Prompt the user to input the cash rendered.
            [/] Validate if the cash is sufficient to cover the total cost.
            [/] If insufficient, repeatedly ask for payment until the amount is valid.
            [/] Calculate and display the change

3. Upload Requirements:
Must be in your own github repository with repo name: Lastname_Functions, filename must be: Lastname_Lab12

'''

#ICE CREAM SHOP MENU: 
menu = [
    ["Flavors", [
        ["F1", "Chocolate Fudge", 35.00],
        ["F2", "Vanilla Bean", 40.00],
        ["F3", "Strawberry Swirl", 40.00],
        ["F4", "Mint Chocolate Chip", 40.00],
        ["F5", "Cookies & Cream", 40.00],

    ]],
    ["Milkshakes", [
        ["M1", "Classic Vanilla Shake", 75.00],
        ["M2", "Chocolate Madness Shake", 75.00],
        ["M3", "Strawberry Breeze Shake", 85.00],
        ["M4", "Caramel Coffee Shake", 90.00],
        ["M5", "Oreo Crunch Shake", 90.00]
    ]],
    ["More Desserts", [
        ["D1", "Ice Cream Cake Slice", 65.00],
        ["D2", "Frozen Cheesecake Slice", 65.00],
        ["D3", "Ice Cream Sandwich", 30.00],
        ["D4", "Chocolate Lava Ice Cream Cup", 60.00],
        ["D5", "Mango Float", 75.00]
    ]],
    ["Beverages", [
        ["B1", "Bottled Water", 15.00],
        ["B2", "Iced Tea", 20.00],
        ["B3", "Soda (Coke, Sprite, Fanta)", 15.00],
        ["B4", "Hot Coffee", 20.00],
        ["B5", "Iced Coffee", 30.00]
    ]]
]

# Display Menu Function: 
def display_menu():
    print("\n--- MENU ---")
    for category, items in menu:
        print(f"\n{category.upper()}: ")
        for code, name, price in items:
            print(f"   {code} - {name}: ₱{price:.2f}/scoop")

# Order Selection Function: 
def get_order():
    order = []  
    cost = 0 
    
    print("\nEnter 'x' to cancel your order.") 

    while True:
        menu_choice = input("\nEnter the code of your order (or 'd' if done ordering): ").upper() 

        if menu_choice == 'X':
            print("Order cancelled. Returning to main menu...\n")
            return "cancelled", 0
        elif menu_choice == 'D':
            if order:
                print("Done ordering, proceeding to check-out... \n")
                return order, cost
            else:
                print("Your order basket is empty. Please enter your order first.")
                continue
        
        item_found = False
        for category, items in menu:
            for code, name, price in items: 
                if menu_choice == code:
                    order.append([name, price])
                    cost += price
                    print(f"{name}: ₱{price:.2f} is added to your order basket.")
                    item_found = True
                    break
            if item_found:
                break

        if not item_found:
            print("Invalid input. Make sure to input a code from the menu only. Try again.")

# Payment Processing Function: 
def payment(User_Payment, total_order_cost):
    if User_Payment >= total_order_cost:
        if User_Payment == total_order_cost:
            print("\nThank you for your payment! Please proceed to the claim section to claim your ice cream.")
            print("Enjoy and come back again!")
        else:
            Change = User_Payment - total_order_cost
            print(f"\nThank you for your payment! Here's your change: ₱{Change:.2f}")
            print("Please proceed to the claim section to claim your ice cream.")
            print("Enjoy and come back again!")
    else:
        print("Insufficient payment. Please try again.\n")
        return("insufficient")

# MAIN MENU:
while True:
    print("Welcome to XC One Scoop Ice cream Shop!")                      
    start = input("Enter '1' to order or '2' to end the order transaction: ") 

    if start not in ["1", "2"]: 
        print("Please enter 1 or 2 only. Try again. \n")
        continue
    elif start == "2":
        print("\nEnding the transaction...")
        break
    else:
        display_menu()

#ORDER SELECTION: Allow the user to choose an item from the menu.
    all_orders = [] 
    total_order_cost = 0
    while True:
        order, cost = get_order()

        if order == "cancelled":
            break
        elif order:
            for item in order:  
                all_orders.append(item)  
                total_order_cost += item[1]  
            break  

#CALCULATE TOTAL AND PAYMENT  PROCESSING: Determine the total cost of the selected item and prompt the user to input the cash rendered.
    if all_orders: 
        #To determine the total cost of the selected items
        print("\n--- Checkout ---")
        print("Order summary:")
        for name, price in all_orders:
            print(f"    {name}: ₱{price:.2f}")

        print(f" Total cost: ₱{total_order_cost:.2f} \n")
        print("Entering the payment transaction...\n")

        #To process the payment:
        while True:
            try:
                print("Please pay to confirm your order.")
                User_Payment = float(input("Payment amount: "))
                User_Payment= payment(User_Payment, total_order_cost)

                if User_Payment == "insufficient":
                    continue

            except ValueError:
                print("Invalid input. Please enter a valid amount for the payment.\n")
            break
    break