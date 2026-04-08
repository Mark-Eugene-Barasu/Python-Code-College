users = {
    'L' : {
        'name' : 'B',
        'surname' : 'R',
        'age' : 12
    },
    'A' : {
        'name' : 'N',
        'surname' : 'P',
        'age' : 15
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username} {user_info}")
    
    # Accessing and printing values from the inner dictionary
    full_name = f"{user_info['name']} {user_info['surname']}"
    age = user_info['age']
    
    print(f"Full Name: {full_name}")
    print(f"Age: {age}")
