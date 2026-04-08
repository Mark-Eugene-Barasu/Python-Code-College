# 3.1 Names Array
print("-----3.1 Names Array-----")

# Define a list of names
names = ['Jack', 'Bob', 'Cee', 'Lee']

# Print each name in the list one at a time
print(names[0])  # Prints 'Jack'
print(names[1])  # Prints 'Bob'
print(names[2])  # Prints 'Cee'
print(names[3], "\n")  # Prints 'Lee' followed by a newline for spacing

# 3.2 Greetings
print("-----3.2 Greetings-----")

# Re-define the same list of names
names = ['Jack', 'Bob', 'Cee', 'Lee']

# Print personalized greetings for each name using f-strings
print(f"Hello, {names[0]} Hope you're having a great day!")
print(f"Hello, {names[1]} Hope you're having a great day!")
print(f"Hello, {names[2]} Hope you're having a great day!")
print(f"Hello, {names[3]} Hope you're having a great day!", "\n")

# 3.3 Your own list
print("-----3.3 Your own list-----")

# Define a list of vehicles (both cars and motorcycles)
vehicles = ['Yamaha', 'Honda', 'Mercedes', 'Audi', 'Ford']

# Print statements expressing interest in various vehicles
print(f"I would love to drive a {vehicles[4]} car.")         # Refers to 'Ford'
print(f"I would like to ride a {vehicles[1]} motorcycle.")   # Refers to 'Honda'
print(f"I would love to own a {vehicles[2]} car.")           # Refers to 'Mercedes'
print(f"I would like to test drive an {vehicles[3]} car.")   # Refers to 'Audi'
print(f"I would like to race a {vehicles[0]} motorcycle.")   # Refers to 'Yamaha'
