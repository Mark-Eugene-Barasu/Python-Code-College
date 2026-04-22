# 1. Moving Items from One List to Another
# Moving Items from One List to Another
unconfirmed_users = ['alice', 'brian', 'candace', 'jose', 'fuzzy', 'khetho']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()  # Remove last user from the list
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)  # Add to the confirmed users list

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(f" - {confirmed_user.title()}")
####################################################################################
# # 2. Removing All Instances of Specific Values from a List
# # Removing All Instances of a Specific Value from a List
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print("\nOriginal list of pets:", pets)

# while 'cat' in pets:
#     pets.remove('cat')  # Remove first occurrence of 'cat'

# while 'rabbit' in pets:
#     pets.remove('rabbit')  # Remove first occurrence of 'rabbit'

# print("Updated list of pets:", pets)
# ####################################################################################
# 3. Filling a Dictionary with User Input
# Filling a Dictionary with User Input
responses = {}
polling_active = True

# while polling_active:
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")

#     # Store the response in the dictionary
#     responses[name] = response

#     repeat = input("Would you like to let another person respond? (yes/no) ")
#     if repeat.lower() == 'no':
#         polling_active = False  # End the poll if the user types 'no'

# # Show the poll results
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}.")
