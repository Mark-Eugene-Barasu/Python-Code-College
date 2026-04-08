# Example 1: Handling the ZeroDivisionError Exception
# This try-except block attempts to divide 5 by 0, which will raise a ZeroDivisionError.
# The except block catches that error and prints a friendly message.
try:
    print(5/0)  
except ZeroDivisionError:
    print("You can't divide by zero!") 


# Example 2: Using try-except Blocks for Division
# This program asks the user to input two numbers and divides them.
# If the user attempts to divide by zero, a error message is shown.

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")  # Prompt for the first number
    if first_number == 'q':                   # Exit if the user enters 'q'
        break
    second_number = input("Second number: ")  # Prompt for the second number
    if second_number == 'q':  
        break
    answer = int(first_number) / int(second_number)
    print(answer)

# Page 194:
try:
    answer = 10/5 # Try to divide the numbers
except ZeroDivisionError:                            # Handle the error 
    print("You can't divide by 0!")  
else:
    print(answer)  # Print the result of the division if no error occurred