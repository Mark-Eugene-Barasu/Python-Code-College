# 5.1 Conditional Tests:
town = "Port Alfred"
print(f"Is town == 'Port Alfred'? I predict True.")
print(town == "Port Alfred")

print(f"\nIs town == 'Port Saint Johns'? I predict False.")
print(town == "Port Saint Johns")


print("1", True or True) # True
print("2", True or False) # True
print("3", False or False) # False

print("4", True and True) # True
print("5", True and False) # False
print("6", False and False) # False

print("7", True or not True) # True
print("8", True or not False) # True
print("9", not True or not True) # False
print("10", not True or not False) # True

print("11", True and not True) # False
print("12", True and not False) # True
print("13", not True and not True) # False
print("14", not True or not False) # True

# 5.2 More Conditional Tests:
numbers = [0, 2, 3, 7, 88, 89, 77, 84]
print( 5 in numbers) # False
print(0 in numbers) # True
print(77 in numbers) # True
print(88 in numbers) # True