# 7-4. Pizza Toppings
print("--- 7-4. Pizza Toppings ---")
while True:
    topping = input("Enter a pizza topping (or 'quit' to stop): ")
    if topping == 'quit':
        break
    print(f"  Adding {topping} to your pizza!")

# 7-5. Movie Tickets
print("\n--- 7-5. Movie Tickets ---")
while True:
    age = input("Enter your age (or 'quit' to stop): ")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("  Your ticket is free!")
    elif age <= 12:
        print("  Your ticket costs $10.")
    else:
        print("  Your ticket costs $15.")

# 7-6. Three Exits (using Pizza Toppings)

# Version 1: conditional test in while statement
print("\n--- 7-6. Version 1: Conditional test in while ---")
topping = ""
while topping != 'quit':
    topping = input("Enter a topping (or 'quit' to stop): ")
    if topping != 'quit':
        print(f"  Adding {topping} to your pizza!")

# Version 2: active variable
print("\n--- 7-6. Version 2: Active variable ---")
active = True
while active:
    topping = input("Enter a topping (or 'quit' to stop): ")
    if topping == 'quit':
        active = False
    else:
        print(f"  Adding {topping} to your pizza!")

# Version 3: break statement
print("\n--- 7-6. Version 3: Break statement ---")
while True:
    topping = input("Enter a topping (or 'quit' to stop): ")
    if topping == 'quit':
        break
    print(f"  Adding {topping} to your pizza!")

# 7-7. Infinity (press CTRL-C to stop)
# print("\n--- 7-7. Infinity ---")
# while True:
#     print("This loop never ends!")
