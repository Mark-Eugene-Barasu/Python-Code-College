# Creating a list of car brands
cars = ['toyota', 'honda', 'ford', 'chevrolet']

# Accessing the first element using index position 0
first_car = cars[0]

# Using f-string to insert the list item into a sentence
message = f"My first car was a {first_car.title()}."

# Printing the message
print("1. generated sentence:", message, "\n")
######################################################
# Starting with a list of motorcycles
motorcycles = ['honda', 'yamaha', 'suzuki']

# Modifying an element (change 'yamaha' to 'ducati')
motorcycles[1] = 'ducati'
print(f"2. Modified list: {motorcycles} ", "\n")

# Adding an element to the end of the list using append()
motorcycles.append('kawasaki')
print(f"3. List after appending 'kawasaki': {motorcycles}", "\n")

# Inserting an element at the beginning of the list using insert()
motorcycles.insert(0, 'harley-davidson')
print(
    f"4. List after inserting 'harley-davidson' at the beginning: {motorcycles}", "\n")

motorcycles.insert(3, 'shadow')
print(
    f"4. List after inserting 'shadow' at the beginning: {motorcycles}", "\n")

# Removing an element by index using del
del motorcycles[2]
print(f"5. List after removing element at index 2: {motorcycles}", "\n")

# Using pop() to remove and return the last item
popped_motorcycle = motorcycles.pop()
print(f"6. List after popping the last element: {motorcycles}", "\n")
print(f"7. Popped motorcycle: {popped_motorcycle}", "\n")

# Using pop() to remove an item from a specific position
first_motorcycle = motorcycles.pop(0)
print(f"8. List after popping the first element: {motorcycles}", "\n")
print(f"9. Popped first motorcycle: {first_motorcycle}", "\n")

# Removing an item by value using remove()
# an error will appear because "ducati" is not in the list
# motorcycles.remove('ducati')
print(f"10. List after removing 'ducati': {motorcycles}", "\n")

# Attempting to remove an item by value that doesn't exist raises an error
# motorcycles.remove('harley')  # Uncommenting this would raise a ValueError

# Final list
print(f"11. Final list of motorcycles: {motorcycles}", "\n")
