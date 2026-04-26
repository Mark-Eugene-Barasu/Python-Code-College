
# Create a Python program that meets the following requirements:
# 1. Use a while loop to repeatedly ask the user to enter a number between 1 and 10, or allow them to type "quit" to exit the program.
# 2. Add a flag to control when the loop should stop. Set the flag to True when the user types "quit" or enters  the number 5.
# 3. Use continue statements to skip to the next iteration if the user enters an invalid input (e.g., something that is not a number) or a number outside the range of 1 to 10.
# 4. Use the break to exit the loop if the user types "quit" or enters the number 5. 
# 5. If the user types "quit", the loop should end immediately.
# 6. If the user enters the number 5, print "You entered 5, exiting the  loop" and then end the loop.

active = True

while active:
    user_input = input("Enter a number between 1 and 10 (or 'quit' to exit): ")

    if user_input == 'quit':
        break

    if not user_input.isdigit():
        print("Invalid input. Please enter a number.")
        continue

    number = int(user_input)
    if 1 <= number <= 10:
        if number == 5:
            print("You entered 5, exiting the loop.")
            # active = False
            break
        else:
            print(f"You entered {number}.")
    else:
        print("Invalid input. Please enter a number between 1 and 10.")
        continue
