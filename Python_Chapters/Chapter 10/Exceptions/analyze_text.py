# Example 4: Analyzing Text
# This program reads a text file and counts the approximate number of words in it.
from pathlib import Path

# Define the path to the file 'alice.txt'
path = Path('C:/Users/lesed/OneDrive/Documents/Code College/WEB BOOTCAMP/2. Python/MyWork/Source_Code/Chapters/Chapter 10/Exceptions/alice.txt')

# Attempt to read the contents of the file
try:
    contents = path.read_text(encoding='utf-8')# Try to read the content of 'alice.txt'
except FileNotFoundError:                      # If the file is not found, print an error message
    print(f"Sorry, the file {path} does not exist.")
else:
    # If the file was successfully read, count the words
    words = contents.split()  # Split the content into a list of words based on whitespace
    num_words = len(words)    # Count the number of words in the list
    print(f"The file {path} has about {num_words} words.")  # Display the word count

    

