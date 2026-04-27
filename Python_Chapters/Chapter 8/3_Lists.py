# Example 1: Function to greet users
def greet_users(names):
    for name in names:
        print(f"Hello, {name.title()}!")        # Prints a greeting for each user

# Passing a List to a Function (greet_users)
usernames = ['alice', 'bob', 'charlie']
greet_users(usernames)                   # Calls greet_users() to print greetings for each user
print()

##############################################################################################

# Example 2: Function to modify a list (moving designs from unprinted to completed)
def add_designs_to_completed(unprinted_designs, completed_designs):
    
    while unprinted_designs:  # Continues until the unprinted designs list is empty
        current_design = unprinted_designs.pop()# Removes the last item from unprinted_designs
        completed_designs.append(current_design)# Adds the item to completed_designs

# Modifying a List in a Function (modifies the original list)
unprinted_designs = ['phone case', 'robot', 'pen holder']
completed_designs = []                                        # Empty list to store completed designs
add_designs_to_completed(unprinted_designs, completed_designs)# Modifies the original list

print("Completed designs:", completed_designs)  
print("Unprinted designs (original list, modified):", unprinted_designs) 
print()


########################################################################################################

# Example 3: Function to prevent modification of the original list
def add_designs_to_completed_without_modifying_original(unprinted_designs, completed_designs):
    unprinted_designs_copy = unprinted_designs.copy()      # Create a copy of the original list
    
    while unprinted_designs_copy:                      # Continues until the copied list is empty
        current_design = unprinted_designs_copy.pop()  # Removes the last item from the copy
        completed_designs.append(current_design)       # Adds the item to completed_designs

    print("unprinted_designs_copy:", unprinted_designs_copy) 

# Preventing a Function from Modifying the Original List
unprinted_designs = ['phone case', 'robot', 'pen holder']
completed_designs = []                                         # Empty list to store completed designs

# Works on a copy of the list
add_designs_to_completed_without_modifying_original(unprinted_designs, completed_designs)  
print("Completed designs:", completed_designs)  
print("Unprinted designs (original list, unchanged):", unprinted_designs)  