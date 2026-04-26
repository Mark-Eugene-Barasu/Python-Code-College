

active = True

while active:
    user_input = input("Do you want to continue? (yes/no) ")
    if user_input.lower().strip() == 'no':
        # active = False
        break  # Exit the loop immediately
    elif user_input.lower().strip() == 'yes':
        print("Continuing the loop...")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")