available_toppings = ['mushrooms', 'pepperoni', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# Check if the list is empty first
if requested_toppings:
    for topping in requested_toppings:
        if topping in available_toppings:
            print(f"Adding {topping}.")
        else:
            print(f"Sorry, we don't have {topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
