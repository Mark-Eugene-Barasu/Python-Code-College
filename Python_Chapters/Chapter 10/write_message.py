#Writing Multiple Lines
from pathlib import Path

contents = "I love playing.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"
contents += "I love eating SWEETS!!!!!!.\n"

path = Path(r'C:\Users\lesed\OneDrive\Documents\Code College\WEB BOOTCAMP\2. Python\MyWork\Source_Code\Chapters\Chapter 10\play.txt')
path.write_text(contents)

