# Available items in store
available_items = ['apple', 'banana', 'carrot', 'pear', 'berry']

# Customer's shopping cart 
shopping_cart = []

# Asking the user to input items they want to add
item1 = input("Enter the first item you want to add to your cart: ").lower()
item2 = input("Enter the second item you want to add to your cart: ").lower()
item3 = input("Enter the third item you want to add to your cart: ").lower()

# Add items to shopping cart based on conditions
if item1 in available_items:
    shopping_cart.append(item1)
    print(f"{item1} has been added to your cart.")
else:
    print(f"Sorry, {item1} is not available in the store.")

if item2 in available_items:
    shopping_cart.append(item2)
    print(f"{item2} has been added to your cart.")
else:
    print(f"Sorry, {item2} is not available in the store.")

if item3 in available_items:
    shopping_cart.append(item3)
    print(f"{item3} has been added to your cart.")
else:
    print(f"Sorry, {item3} is not available in the store.")

# Checking for special items (e.g., discounts) before displaying the shopping cart
if 'banana' in shopping_cart:
    print("Banana is on sale! Discount applied.")

# Displaying the shopping cart content
print("\nYour shopping cart contains the following items:")
print(shopping_cart)

# No additional print statements for adding items to the purchase
if not shopping_cart:
    print("Your shopping cart is empty! Please add some items.")