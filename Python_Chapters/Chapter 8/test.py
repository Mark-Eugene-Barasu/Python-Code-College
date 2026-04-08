# def greet(name, age):
#     print(f"Nice to meet you {name}, you are {age} years old.")

# greet("Lee", 30)
# greet("Lee", 30)
# greet("Le", 10)

########################################
# print("-----Positional Arguments (need to be in order)-------")
# def create_account(username, password, email):
#     print(f"Account created for {username}")
#     print(f"Password: {password}")
#     print(f"Email: {email} \n")

# print("------Correct order-----")
# create_account('Lee', 5252, 'lee@gmail.com')

# print("----incorrect order---")
# create_account('lee@gmail.com', 'Lee', 5252)

##########################################################

# print("-----Keyword Arguments (doesn't need the order)-------")

# def create_account(username, password, email):
#     print(f"Account created for {username}")
#     print(f"Password: {password}")
#     print(f"Email: {email} \n")

# print("------Positional Args-----")
# create_account('Lee', 5252, 'lee@gmail.com')

# print("------Keyword Args 1.-----")
# create_account(username='Lee', password=5252, email='lee@gmail.com')

# print("------Keyword Args 2.-----")
# create_account(password=5252, email='lee@gmail.com', username='Lee')

#################################################
print("-----Keyword Arguments (doesn't need the order)-------")

def create_account(username ='Lee', password=5252, email='lee@gmail.com'):
    print(f"Account created for {username}")
    print(f"Password: {password}")
    print(f"Email: {email} \n")

print("------Calling the default values-----")
create_account()

print("------1. Defaults-----")
create_account(username='AA', password=0000, email='aa@gmail.com')

print("------2. Defaults-----")
create_account(password=1212, email='pp@gmail.com', username='Vee')
