from pathlib import Path


def count_words(filename):
    """Count the approximate number of words in a file."""
    path = Path(filename)

    try:
        # 'encoding' is used when files are created on other systems
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' does not exist.")
    else:
        # .split() breaks a string up into a list wherever it sees spaces
        words = contents.split()
        num_words = len(words)
        print(f"The file '{filename}' has about {num_words} words.")


# Example of looping safely through multiple files
books = ['C:/Users/mark0/OneDrive/Desktop/Code College/Python/Python_Chapters/Chapter 10/pi_digits.txt',
        'siddhartha.txt', 'moby_dick.txt']
for book in books:
    count_words(book)
