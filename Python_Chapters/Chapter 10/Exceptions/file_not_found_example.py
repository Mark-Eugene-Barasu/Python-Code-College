# Example 3: Handling the FileNotFoundError Exception
# This program tries to read a file that doesn't exist. If the file is missing,
# it raises a FileNotFoundError, and we handle it with a friendly error message.
from pathlib import Path

# Define the path to the file 'alice.txt'
path = Path('alice.txt')

# Attempt to read the contents of the file
try:
    contents = path.read_text(encoding='utf-8')  # This line tries to open and read 'alice.txt'
except FileNotFoundError:                        # Catch the exception if the file doesn't exist
    print(f"Sorry, the file {path} does not exist.") 


    
