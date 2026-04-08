# Creating the pi_digits.txt File and Python Script (file_reader.py)
from pathlib import Path

# Define the path to the file inside the 'text_files' folder
path = Path('C:/Users/lesed/OneDrive/Documents/Code College/WEB BOOTCAMP/2. Python/MyWork/Source_Code/Chapters/Chapter 10/pi_digits.txt')

# Read the entire contents of the file and remove trailing whitespace
contents = path.read_text().rstrip()

# Split the content into lines
lines = contents.splitlines()

# Access and print each line
for line in lines:
    print(line)

