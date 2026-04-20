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
    print(f"The key is: \"{a}\" this is the value \"{b}\"")


for value in student_info.values():
    print(value)

print(student_info["name"])
print(student_info["fruits"][1])
print(list(student_info.values())[2])
