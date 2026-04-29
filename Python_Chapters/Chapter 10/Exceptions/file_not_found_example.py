# Example 3: Handling the FileNotFoundError Exception
# This program tries to read a file that doesn't exist. If the file is missing,
# it raises a FileNotFoundError, and we handle it with a friendly error message.
from pathlib import Path

# Define the path to the file 'alice.txt'
path = Path(r'C:\Users\mark0\OneDrive\Desktop\Code College\Python\Python_Chapters\Chapter 10\Exceptions\alice.txt')  # This file does not exist, which will trigger the exception

# Attempt to read the contents of the file
try:
    contents = path.read_text(encoding='utf-8')  # This line tries to open and read 'alice.txt'
    print("we found the file and read it successfully!")
except FileNotFoundError:                        # Catch the exception if the file doesn't exist
    print(f"Sorry, the file {path} does not exist.")


    
