# checking for equality
a = 10
b = 20
print(a == b)

# Checking for inequality
print(a != b)

# Using "and" to check multiple conditions
x = 5
y = 10
print(x > 2 and y < 15)

# Using 'or' to check multiple conditions
print(x < 2 or y > 5)

# Checking whether a value is not in a list
numbers = [1, 2, 3, 4, 5]
print(6 not in numbers)

# Boolean expressions
is_raining = False
has_umbrella = True
print(is_raining and has_umbrella)

# Test in Python Shell
# Ignoring Case When Checking for Equality
str1 = "hello"
str2 = "HELLO"
print(str1.lower() == str2.lower())

# Numerical Comparisons
a = 25
b = 30
print(a < b)
print(a == b)
print(a >= b)

# Using "and" to check multiple conditions
age = 18
is_student = True
print(age >= 18 and is_student)

# Checking Whether a value is in a list
colors = ["red", "green", "blue"]
print("green" in colors)
print("yellow" in colors)

# Using if and else statement
# 1. Example with Multiple if Statements:
temperature = 30

if temperature > 25:
    print("It's hot outside.")
if temperature < 40:
    print("It's a warm day.")
if temperature == 30:
    print("The temperature is exactly 30°C")

# 2. Example with if Statements and if-else Statements:
color = "blue"

if color == "red":
    print("The color is red!")
else:
    print("The color is not red.")

# 3. Example with Multiple if-elif Statements:
grade = 87

if grade >= 90:
    print("You got an A!")
elif grade >= 80:
    print("You got a B!")
elif grade >= 70:
    print("You got a C!")
elif grade >= 60:
    print("You got a D!")


# Using if Statements with Lists
# Available items in store
available_items = ["apple", "banana", "carrot", "pear", "berry"]

# Customer's shopping cart
shopping_cart = []

# Asking the user to input items they want to add
item1 = input("Enter the first item you want to add to your cart: ").lower()
item2 = input("Enter the second item you want to add to your cart: ").lower()
item3 = input("Enter the third item you want to add to you cart: ").lower()

# Add items to shopping cart based on conditions
if item1 in available_items:
    shopping_cart.append(item1)
    print(f"{item1} has been added to you cart.")
else:
    print(f"Sorry, {item1} is not available in the store.")

if item2 in available_items:
    shopping_cart.append(item2)
    print(f"{item2} has been added to you cart.")
else:
    print(f"Sorry, {item2} is not available in the store.")

if item3 in available_items:
    shopping_cart.append(item3)
    print(f"{item3} has been added to your cart.")
else:
    print(f"Sorry, {item3} is not available in the store.")


# Checking for special items (e.g., discounts) before displaying the shopping cart
if "banana" in shopping_cart:
    print("Banana is on sale! Discount applied.")

# Displaying the shopping cart content
print("\nYour shopping cart contains the following items:")
print(shopping_cart)

# No additional print statements for adding items to the purchase
if not shopping_cart:
    print("Your shopping cart is empty! Please add some items.")