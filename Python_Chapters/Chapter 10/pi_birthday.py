from pathlib import Path

path = Path(r'C:\Users\mark0\OneDrive\Desktop\Code College\Python\Python_Chapters\Chapter 10\pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()  # Remove leading and trailing whitespace

birthday = input("Enter your birthday, in the form mmddyy: ")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

