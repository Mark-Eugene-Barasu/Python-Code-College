print('---1. Using range() function---')
for number in range(5):  
    print(number)

print("\n")
print('---2. Using range() with list()---')
even_numbers = list(range(0, 11, 2))  
print(even_numbers)

print("\n")
print('---3. Square Root Example (Squares of Numbers)---')
squares = []
for number in range(1, 4): 
    square = number ** 2
    squares.append(square)
print(squares)

print("\n")
print('--4. Using min(), max(), and sum()--')
numbers = [10, 20, 30, 40, 50]
print("Min:", min(numbers))  
print("Max:", max(numbers))  
print("Sum:", sum(numbers))  

print("\n")
print('---5. List Comprehensions--')
doubled_numbers = [number * 2 for number in range(1, 6)]
print(doubled_numbers)

#####################################################################################
print("\n")
#6. Original list of fruits
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

#7. Slicing a list: Get the first three fruits
sliced_fruits = fruits[:3]

print('---8. Looping through a slice: Print each fruit in the slice---')
print("First three fruits:")
for fruit in sliced_fruits:
    print(fruit)

# Copying a list: Make a copy of the entire list
copied_fruits = fruits[:]

# Modify the original list and show both lists
fruits.append('fig')

print("\n---11. Original list after adding a fruit:---")
print(fruits)

print("\n---12. Copied list (unchanged):---")
print(copied_fruits)

