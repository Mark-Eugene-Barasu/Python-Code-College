#A List of Dictionaries:
# List of dictionaries, each representing a car's details
cars = [
    {'make': 'Toyota', 'model': 'Corolla', 'color': 'blue'}, # item one (index 0)
    {'make': 'Honda', 'model': 'Civic', 'color': 'red'}, # item two (index 1)
    {'make': 'Ford', 'model': 'Mustang', 'color': 'black'} # item three (index 2)
]

# Loop through the list of dictionaries and print each car's details
for car in cars:
    print(f"I drive a {car['make']} {car['model']}, that has the color {car['color']}")
print()
############################################################################
#A List in a Dictionary:
# Dictionary containing a list of car colors
garage = {
    'colors': ['blue', 'red', 'black', 'white', 'green'],
    'location': 'San Francisco'
}

# Accessing and printing the list of car colors in the dictionary
print(f"Garage Location: {garage['location']}")
print("Available Colors for Cars:")
for color in garage['colors']:
    print(f"- {color}")

#############################################################################
# A Dictionary in a Dictionary
# Define the dictionary
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
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    location = user_info['location']
    
    print(f"Full Name: {full_name}")
    print(f"Location: {location}")



