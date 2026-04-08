#Working with a File’s Contents
from pathlib import Path

# Define the path to the file
path = Path(r'C:\Users\lesed\OneDrive\Documents\Code College\WEB BOOTCAMP\2. Python\MyWork\Source_Code\Chapters\Chapter 10\pi_digits.txt')

# Read the entire contents of the file
contents = path.read_text()

# Split the content into lines
lines = contents.splitlines()

# Initialize an empty string to hold the digits
pi_string = ''

# Loop through each line and concatenate it to pi_string
for line in lines:
    pi_string += line  

# Print the concatenated string
print(f"Pi String: {pi_string}")

# Print the length of the string
print(f"String Length: {len(pi_string)}")