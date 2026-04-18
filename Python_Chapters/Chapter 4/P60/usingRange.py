# 4.3 Counting to twenty:
for x in range(1, 21):
    print(x)

# 4.4 Thirty:
for y in range(0, 31):
    print(y)

# 4.5 Summing a Million
numbers = list(range(1, 1000001))

print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Sum: {sum(numbers)}")

# 4.6 Odd numbers
odd_numbers = list(range(1, 21, 2))
print(odd_numbers)


# 4-7. Threes
threes = list(range(3, 31, 3))
for number in threes:
    print(number)

# 4-8. Cubes
cubes = []
for value in range(1, 11):
    cube = value**3
    cubes.append(cube)

for cube in cubes:
    print(cube)

# 4-9. Cube Comprehension
cubes_comprehension = [value**3 for value in range(1, 11)]
print(cubes_comprehension)


