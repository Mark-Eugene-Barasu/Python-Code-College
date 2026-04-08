# String Formatting in Python (Old Style)
name = "Alice"
age = 25
message = "Name: %s, Age: %d" % (name, age)
print(message)      #Name: Alice, Age: 25

# String Formatting in Python (Using .format())
name = "Sam"
age = 12
gender = "female"
message = "Name: {}, Age: {}, Gender: {}".format(name, age, gender)
print(message)       #Name: Sam, Age: 12, Gender: female

# String Formatting in Python (Using f-strings)
name = "Paul"
AGE = 36
dogName = "Jack"
message = f"Name: {name}, Age: {age}, DogName: {dogName}"
print(message)       #Name: Paul, Age: 36, DogName: Jack

