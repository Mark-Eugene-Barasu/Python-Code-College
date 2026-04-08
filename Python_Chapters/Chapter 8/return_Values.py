#Here’s a simple example incorporating Return Values, Making an Argument Optional, 
# Returning a Dictionary, and Using a Function with a While Loop:

print("---Person Object----")
# Define three parameters: first_name, last_name, and age (optional)
def build_person(first_name, last_name, age=None):
    """Return a dictionary with person's information."""
    person = {'first': first_name, 'last': last_name}
    
    # If an age is provided, add it to the dictionary
    if age:
        person['age'] = age
        
    # Return the dictionary
    return person


def greet_person():
    while True:
        # Ask for first name, exit loop if user enters 'q'
        first_name = input("Enter first name (or 'b' to quit): ")
        if first_name == 'b':
            break
        
        # Ask for last name, exit loop if user enters 'q'
        last_name = input("Enter last name: ")
        if last_name == 'b':
            break
        
        # Ask for age, make it optional (default to None if not provided)
        age = input("Enter age (optional): ")
        if age == '':
            age = None  # Default age to None if not provided
        else:
            age = int(age)  # Convert age to an integer if provided

        # Call the build_person function to create a dictionary with user details
        person = build_person(first_name, last_name, age)
        
        # Display the greeting with person's name
        print(f"Hello, {person['first']} {person['last']}!")
        
        # If age is provided, display it as well
        if age:
            print(f"Age: {person['age']}")

# Call the greet_person function to start the program
greet_person()