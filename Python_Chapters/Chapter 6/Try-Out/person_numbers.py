# 6.1 to 6.3 (page 98)

# 6-1. Person
person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "city": "Berlin"
}

for key, value in person.items():
    print(f"{key}: {value}")

# 6-2. Favorite Numbers
favorite_numbers = {
    "John": 7,
    "Jane": 13,
    "Mark": 42,
    "Sara": 5,
    "Tom": 99
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}")

# 6-3. Glossary
glossary = {
    "variable": "A container for storing data values.",
    "loop": "A sequence of instructions that repeats until a condition is met.",
    "function": "A reusable block of code that performs a specific task.",
    "dictionary": "A collection of key-value pairs.",
    "list": "An ordered and changeable collection of items."
}

for word, meaning in glossary.items():
    print(f"{word}:\n  {meaning}\n")
