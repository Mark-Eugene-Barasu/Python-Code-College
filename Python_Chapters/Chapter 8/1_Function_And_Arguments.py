#Here's an example that defines a function, passes information to it, and demonstrates arguments and parameters:
# Define the function
def greet(name, age):
    """Display a greeting message with name and age."""
    print(f"Hello, {name}! You are {age} years old.")

# Passing information to the function
greet('Alice', 30)  
greet('Bob', 25)    

################################################################################################
#The code defines a function create_account(username, password, email) that accepts three parameters: 
# username, password, and email. The function prints a message indicating the account has been created 
# and displays the associated username, password, and email.
def create_account(username, password, email):
    print(f"\nAccount created for {username}.")
    print(f"Password: {password}")
    print(f"Email: {email}")

# Correct order: 
create_account('john_doe', 'mypassword', 'john@example.com')

# Incorrect order: 
create_account('mypassword', 'john_doe', 'john@example.com')

################################################################################################
#The function register_product(product_name, product_type, price) is defined to accept three parameters: 
# product_name, product_type, and price. It prints information about the product, including its name, type, and price.
def register_product(product_name, product_type, price):
    print(f"\nProduct: {product_name}")
    print(f"Type: {product_type}")
    print(f"Price: ${price}")

# Using positional arguments
register_product('Laptop', 'Electronics', 999.99)

# Using keyword arguments (order doesn't matter)
register_product(product_name='Laptop', product_type='Electronics', price=999.99)

# Changing the order with keyword arguments
register_product(price=999.99, product_type='Electronics', product_name='Laptop')

#############################################################################################
#This code defines a function called sandwich that takes two parameters: bread_type and filling. Both parameters have default values
def sandwich(bread_type='whole wheat', filling='ham'):
    print(f"\nMaking a {bread_type} sandwich with {filling}.")

# Using default values
sandwich()

# Providing custom values
sandwich(bread_type='sourdough', filling='turkey')

# Using keyword arguments and changing the order
sandwich(filling='cheese', bread_type='rye')

####################################################################################
#This code defines a function called register_user that takes three parameters, username, age, email
def register_user(username, age, email):
    print(f"\nUser: {username}")
    print(f"Age: {age}")
    print(f"Email: {email}")

# Correct function call
register_user('john_doe', 25, 'john@example.com')

# Missing arguments (will raise an error)
#register_user('jane_doe')  # Uncommenting this line will raise an error

# Extra arguments (will raise an error)
# register_user('alex_smith', 30, 'alex@example.com', 'extra_arg')  # Uncommenting this line will raise an error


