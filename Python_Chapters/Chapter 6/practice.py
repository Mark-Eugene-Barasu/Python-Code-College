student_info = {
    "name": "Alice",
    "age": 22,
    "course": "Computer Science",
    "fruits": ["mango", "orange"]
}


# Accessing the value using the keys
print(student_info["age"])

# Adding new key-value pair
student_info["graduation_year"] = 2023
student_info["gender"] = "female"

# print the updated dictionary
print(student_info)

# looping through a dictionary
for a, b in student_info.items():
    print(f"The key is: \"{a}\" and the value is \"{b}\"")


for value in student_info.values():
    print(value)

print(student_info["name"])
print(student_info["fruits"][1])
print(list(student_info.values())[2])
print(student_info.get("house"))  # doesn't exist therefore : None
# doesn't exist, returns default
print(student_info.get("major", "Undeclared"))

student_scores = {
    "Sajjad": {"math": 100, "English": 95},
    "David": {"math": 95, "English": 100}
}

# Accessing nested dictionary values
print(f"All the keys => {student_scores.keys()}  \nAll the values => {student_scores.values()}")
print(student_scores["Sajjad"]["math"])  # Output: 100
print(student_scores["David"]["English"])  # Output: 100}
