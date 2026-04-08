# Person dictionary
person = {
    'name': 'Alice',
    'age': 30,
}

# Looping through all key-value pairs
for key, value in person.items():
    print(f"key and value - {key}: {value}")
print()

# Looping through all keys
for key in person.keys():
    print("display the key:", key)
print()
################################################################################
# Favorite Colors dictionary
favorite_colors = {
    'Bob': 'blue',
    'Alice': 'green',
    'Charlie': 'red',
}

# Looping through keys in a particular order (alphabetically)
for name in sorted(favorite_colors.keys()):
    print("display the keys:",name)


print()
# Looping through all values in the dictionary
for color in favorite_colors.values():
    print("display the values:", color)

    