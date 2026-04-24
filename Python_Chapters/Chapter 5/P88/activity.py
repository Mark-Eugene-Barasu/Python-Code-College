# 5-8 & 5-9 Hello Admin

usernames = ['admin', 'jaden', 'alice', 'bob', 'charlie']

# Check if empty
if not usernames:
    print("We need to find some users!")
else:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")

print('=' * 50 + '\n')

# 5-9 Empty users test
usernames = []
if not usernames:
    print("We need to find some users!")
print('=' * 50 + '\n')

# 5-10 Checking Usernames (case insensitive)
current_users = ['john', 'alice', 'bob', 'charlie', 'admin']
new_users = ['bob', 'DAVE', 'Alice', 'eve', 'frank']

# Lowercase copy for comparison
current_users_lower = [user.lower() for user in current_users]
# print([user.lower().capitalize() for user in new_users])

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(
            f"Sorry '{new_user}', that username is already taken. Please enter a new username.")
    else:
        print(f"'{new_user}' is available.")

print('=' * 50 + '\n')

# 5-11 Ordinal Numbers
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
