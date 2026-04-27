# function and arguments

# Positional arguments (the order matters)

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# greet('Sedii', 30)  # This will work correctly
greet("Alice", 25)  # This will cause an error because the arguments are in the wrong order     

################################################################

# Keyword arguments (the order does not matter)

def car_product(car_name, car_color, car_price):
    print(f"\nName: {car_name}")
    print(f"Color: {car_color}")
    print(f"Price: ${car_price}")

# Using keyword arguments (order doesn't matter)
car_product(car_name='Toyota', car_color='white', car_price=1000.00)

# Changing the order with keyword arguments
car_product(car_color='Red', car_name='Toyota', car_price=1000.00)

# Avoiding arguments errors

# Missing arguments (will raise an error)
# car_product('Benz')  # Uncommenting this line will raise an error

# Extra arguments (will raise an error)
# car_product('BMW', "orange", 1_000_000, 'extra_arg')  # Uncommenting this line will raise an error


##################################################################

# Default values for parameters (order does not matter)


def sandwich(bread_type='whole wheat', filling='ham'):
    print(f"\nMaking a {bread_type} sandwich with {filling}.")


# Using default values
sandwich()

# Providing custom values   
sandwich(bread_type='sourdough', filling='turkey')

# Using keyword arguments and changing the order
sandwich(filling='cheese', bread_type='rye')

##################################################################

# Avoiding arguments errors
# This code defines a function called register_user that takes three parameters, username, age, email


def register_user(username, age, email):
    print(f"\nUser: {username}")
    print(f"Age: {age}")
    print(f"Email: {email}")


# Correct function call
register_user('john_doe', 25, 'john@example.com')

# Missing arguments (will raise an error)
# register_user('jane_doe')  # Uncommenting this line will raise an error

# Extra arguments (will raise an error)
# register_user('alex_smith', 30, 'alex@example.com', 'extra_arg')  # Uncommenting this line will raise an error
