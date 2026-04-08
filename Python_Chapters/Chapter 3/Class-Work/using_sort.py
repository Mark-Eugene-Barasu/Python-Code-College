#Sample list
cars = ['bmw', 'audi', 'toyota', 'subaru']

#Sorting the list permanently
cars.sort()
print("1. Sorted list(ascending):", cars, "\n")

#Sorting the list in reverse order
cars.sort(reverse=True)
print("2. Sorted list(descending):", cars, "\n")

#Reversing the order of the list
cars.reverse()
print("3.Reversed cars list:", cars, "\n")
########################################################
#Using sorted() to display the list temporarily sorted
original_cars = ['bmw', 'audi', 'toyota', 'subaru']
print("4. Original list:", original_cars)
print("5. Sorted list temporarily:", sorted(original_cars), "\n")

# Reversing the orginal list
original_cars.reverse()
print("6.Reversed orginal list:", original_cars, "\n")

#Finding the length of the list
print("7. Length of the list:", len(cars), "\n")

print("-----------------Trying to access an index that doesn't exist----------------------")
#Accesing a value that doesn't exist
motorcycles = ['honda', 'yamaha', 'suzuki']

#Trying to access an index that doesn't exist
print(motorcycles[3])
print(motorcycles)