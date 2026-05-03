#Writing Multiple Lines
from pathlib import Path

contents = "I love playing.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"
contents += "I love computers\n"

path = Path(r'C:\Users\mark0\OneDrive\Desktop\Code College\Python\Python_Chapters\Chapter 10\messages.txt')
path.write_text(contents)

