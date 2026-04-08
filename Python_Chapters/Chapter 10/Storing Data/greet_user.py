#Storing User Data and Greeting Them
from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        # If the file exists, read the contents and return the username
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    # Save the new username to the file in JSON format
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    
    if username:
        # If a username is found, greet the user
        print(f"Welcome back, {username}!")
    else:
        # If no username is found, ask for a new one and store it
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

# Call the greet_user function to start the process
greet_user()
