# 1. Defining a dictionary
alien_0 = {
    'color': 'green', 
    'points': 5
}

# 2. Accessing and Modifying
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'  # Changing the value
print(f"The alien is {alien_0['color']}.")

# 3. Adding new information
alien_0['x_pos'] = 0
alien_0['speed'] = 'medium'

# 4. Looping through all information
print("\nAlien Details:")
for key, value in alien_0.items():
    print(f" - {key.title()}: {value}")
