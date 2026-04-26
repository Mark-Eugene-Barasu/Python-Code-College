
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