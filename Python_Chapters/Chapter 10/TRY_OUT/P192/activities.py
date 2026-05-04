# Chapter 10 Exercises: 10-4 Guest and 10-5 Guest Book
# These programs demonstrate file I/O operations in Python:
# - Prompting user for input with input()
# - Writing strings to files using open() in 'w' mode (overwrites if exists)
# - Using while loops for repeated input collection
# - Appending names to a list before batch-writing to file
# Files guest.txt and guest_book.txt will be created in the current working directory when run.

print('=== Exercise 10-4: Guest ===')
print('This program prompts for one name and writes it to guest.txt')

# Prompt the user for their name - input() reads a line from stdin and strips newline
name = input('Please enter your name: ')
print(f'Hello, {name}! Your name will be saved to guest.txt.')

# Open file in write mode ('w'): creates new file or overwrites existing; returns file object
with open('./Python_Chapters/Chapter 10/TRY_OUT/P192/guest.txt', 'w') as file:
    # Write the name to the file followed by a newline - write() returns bytes written
    file.write(name + '\n')

print('Name written to guest.txt successfully!')

print('=== Exercise 10-5: Guest Book ===')
print('This program collects multiple names in a loop until "quit" is entered,')
print('then writes all names to guest_book.txt, one per line.')

# Initialize empty list to store all guest names
guest_names = []

# While loop: continues until user enters 'quit' (case-sensitive)
print('Enter guest names (type "quit" when finished):')
while True:
    # Prompt for name; strip whitespace for clean input
    name = input('Enter a name: ').strip()

    # Break loop if user wants to quit
    if name.lower() == 'quit':
        break

    # Add name to list
    guest_names.append(name)
    print(f'Added {name} to the guest book.')

# If names collected, write to file
if guest_names:
    # 'w' mode overwrites; each write adds content
    with open('./Python_Chapters/Chapter 10/TRY_OUT/P192/guest_book.txt', 'w') as file:
        # Loop through list and write each name + newline
        for name in guest_names:
            file.write(name + '\n')
    print('All names written to guest_book.txt successfully!')
    print('Guests:', ', '.join(guest_names))
else:
    print('No names entered.')

print('Program complete. Check guest.txt and guest_book.txt in the current directory.')

# Run command: cd "Python_Chapters/Chapter 10/TRY_OUT/P192" && python activities.py
# Files created in P192!

"""
File open() modes summary:
'r': Read (default) - open existing file for reading, error if not exist
'w': Write - create new/overwrite existing file for writing
'a': Append - add to end of existing file (create if not exist)
'r+': Read+Write - open existing for both reading/writing (error if not exist)
Examples:
open('file.txt', 'r') # Read only
open('file.txt', 'w') # Write (truncates)
open('file.txt', 'a') # Append
open('file.txt', 'r+') # Read/write
Always use 'with' statement: auto-closes file
"""