users = {
    'jdoe': {
        'first_name': 'John',
        'last_name': 'Doe',
        'location': 'New York'
    },
    'jsmith': {
        'first_name': 'Jane',
        'last_name': 'Smith',
        'location': 'Los Angeles'
    }
}
# Looping through the outer dictionary to get user data
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    
    # Accessing and printing values from the inner dictionary
    full_name = f"{user_info['first_name']} {user_info['last_name']} {user_info['location']}"
    print(full_name)
 