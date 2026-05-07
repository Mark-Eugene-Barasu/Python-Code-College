prompt = "\nPlease enter your age to see the ticket price."
prompt += "\n(Enter '0' to finish): "

# Using a flag to control the loop
active = True

while active:
    age_input = input(prompt)

    # Convert input to integer for comparison
    age = int(age_input)

    if age == 0:
        active = False
    elif age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")

print("\nThank you for visiting the theater!")

