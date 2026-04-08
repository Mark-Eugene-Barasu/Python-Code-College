
# Asking for a number with a prompt
number = input("Please enter a number: ")

# Converting the input to an integer
number = int(number)

# Checking if the number is even or odd using the modulo operator
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

