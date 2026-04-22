# 5-1 Conditional Tests
# Test various conditional expressions with predictions

car = 'subaru'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs car != 'toyota'? I predict True.")
print(car != 'toyota')

print("\nIs len(car) == 6? I predict True.")
print(len(car) == 6)

print("\nIs len(car) > 5? I predict True.")
print(len(car) > 5)

print("\nIs car.lower() == 'subaru'? I predict True.")
print(car.lower() == 'subaru')

print("\nIs car.upper() == 'SUBARU'? I predict True.")
print(car.upper() == 'SUBARU')

print("\nIs 'sub' in car? I predict True.")
print('sub' in car)

print("\nIs 'bmw' in car? I predict False.")
print('bmw' in car)

print("\nIs car == 'Subaru'? I predict False.")
print(car == 'Subaru')

print("\nIs len(car) < 6? I predict False.")
print(len(car) < 6)

print("\nIs 5 not in [1,2,3,4,5]? I predict False.")
print(5 not in [1, 2, 3, 4, 5])

print("\nIs 6 not in [1,2,3,4,5]? I predict True.")
print(6 not in [1, 2, 3, 4, 5])
