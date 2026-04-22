

# used_colors = ['red', 'yellow', 'blue', 'green', 'purple', 'black']
# confirmed_colors = []

# while used_colors:
#     current_color = used_colors.pop()  # Remove last user from the list
#     print(f"Verifying user: {current_color.title()}")
#     confirmed_colors.append(current_color)  # Add to the confirmed users list

# print("\nThe following colors have been confirmed:")
# for confirmed_color in confirmed_colors:
#     print(f" - {confirmed_color.title()}")



# print(used_colors)
# print(confirmed_colors)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# # 2. Removing All Instances of Specific Values from a List
# # Removing All Instances of a Specific Value from a List
# cars = ['Benz', 'BMW', 'Benz', 'Polo', 'BMW', 'Honda', 'BMW']
# print("\nOriginal list of cars:", cars)

# while 'BMW' in cars:
#     cars.remove('BMW')  # Remove first occurrence of 'BMW'
#     # del cars["BMW"]

# while 'Benz' in cars:
#     cars.remove('Benz')  # Remove first occurrence of 'Benz'

# print("Updated list of cars:", cars)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 3. Filling a Dictionary with User Input
# Filling a Dictionary with User Input
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False  # End the poll if the user types 'no'

# Show the poll results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
