
active = True

while active:
    message = input("Tell me something, and I will repeat it back to you: ")
    print(f"You said: \"{message}\"")

    repeat = input("Would you like to say something else? (yes/no) ")
    if repeat.lower().strip() == 'no':
        # active = False  # End the loop if the user types 'no'
        break