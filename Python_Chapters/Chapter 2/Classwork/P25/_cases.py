
# 2.3 String Operations and Methods
Eric = "  Hello Eric, would you like to learn Python today?  "

# 2.4 String Methods
print(Eric.lower())  # Output: hello eric, would you like to learn python today?
print(Eric.upper())  # Output: HELLO ERIC, WOULD YOU LIKE TO LEARN PYTHON TODAY?
print(Eric.title())  # Output: Hello Eric, Would You Like To Learn Python Today?
print(Eric.strip())  # Output: Hello Eric, would you like to learn Python today

# 2.5 famous quote
famous_quote = 'Albert Einstein once said, "A person who never made a mistake never tried anything new."'
print(famous_quote)  # Output: Albert Einstein once said, "A person who never made a mistake never tried anything new."

# 2.6 Famous Quote 2
famous_person = "Albert Einstein"
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
print(message)  # Output: Albert Einstein once said, "A person who never made a mistake never tried anything new."

# 2.7 Stripping Names
name = " \n\t  Mark   "
print(name.strip())  # Output: Mark
print(name.lstrip())  # Output: Mark
print(name.rstrip())  # Output: Mark

# 2.8 File Extensions
filename = "example_document.txt"
website = "https://www.example.com"
print(filename.removesuffix(".txt"))  # Output: example_document
print(website.removeprefix("https://www."))  # Output: example.com