# A simple program that asks the user if they want to continue or quit

# Initialize the flag variable
active = True

# Start the while loop
while active:
    # Ask the user for input
    user_input = input("Do you want to keep going? (yes/no): ").lower()

    # Check the user's response
    if user_input == 'no':
        active = False  # Set the flag to False to stop the loop
        print("Goodbye!")
    elif user_input == 'yes':
        print("Let's keep going!")
    else:
        print("Please enter 'yes' or 'no'.")

###################################################################################
# Flag to control the loop
# active = True

# while active:
#      # Ask the user for input
#     number = input("Enter a number between 1 and 10 (or type 'quit' to exit): ")

#     if number.lower() == 'quit':
#         active = False   # Set flag to False to stop the loop
#         break            # Exit the loop early if the user types 'quit'
    
#     # Check if the input is a valid number
#     if not number.isdigit():
#         print("That's not a valid number. Please enter a number.")
#         continue          # Skip the rest of the loop and ask for input again

#     number = int(number)  # Convert the input to an integer

#     if number < 1 or number > 10:
#         print("The number is out of range. Please try again.")
#         continue          # Skip the rest of the loop if the number is out of range
    
#     print(f"You entered {number}.")
#     if number == 5:
#         print("You entered 5, exiting the loop.")
#         active = False    # Set the flag to False to stop the loop
#         break             # Exit the loop when the number is 5

