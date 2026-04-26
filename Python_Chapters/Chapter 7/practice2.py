# Using a while loop with list and dictionary
# Removing all occurrences of 'BMW' and 'Benz' from the list of cars


cars = ['Benz', 'BMW', 'Benz', 'Polo', 'BMW', 'Honda', 'BMW']
print("\nOriginal list of cars:", cars)

while 'BMW' in cars:
    cars.remove('BMW')  # Remove first occurrence of 'BMW'
    # del cars["BMW"]   

while 'Benz' in cars:
    cars.remove('Benz')  # Remove first occurrence of 'Benz'

print("Updated list of cars:", cars)