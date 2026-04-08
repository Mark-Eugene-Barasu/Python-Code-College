# def get_formatted_name(first, last):
#     """Generate a neatly formatted full name."""
#     full_name = f"{first} {last}"
#     return full_name.title()

# # This function takes a first, middle, and last name, combines them into a full name, 
# # and returns the formatted name with proper capitalization.

# def get_formatted_name(first, middle, last):
#     """Generate a neatly formatted full name."""
#     full_name = f"{first} {middle} {last}"
#     return full_name.title()

# This function now makes the middle name optional, and formats the full name 
# accordingly depending on whether the middle name is provided.

def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
