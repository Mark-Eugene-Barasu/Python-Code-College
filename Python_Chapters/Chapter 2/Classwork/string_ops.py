#Concatenation: Combining two or more strings into one.
greeting = "Hello"
name = "Alice"
print("1. Concatenation:", greeting + " " + name)  

#Repetition: Repeating a string multiple times.
print("2. Repetition:","Python! " * 3) 

#Slicing: Extracting a portion of a string.
print("3. Slicing:","Hello, python!"[7:12])  

#Escape Characters: Using special characters like newline (\n) and tab (\t).
print("4. Escape Characters:", "Hello \n how are you \n\t Indented Line")
print("4. Escape Characters:", "\nHello \n\t Hello World \n\t\tHello Python \n")

#String Length: Using the len() function to find the length of a string.
print("5. String Length", len("Hello, Alice!"))  

#Indexing: Accessing individual characters in a string (starting from 0).
print("6. Indexing:", "python"[2])  

#Negative Indexing: Accessing characters from the end of the string.
print("7. Negative Indexing:","Hello"[-1]) 

#String Comparison: Comparing strings using comparison operators.
print("8. String Comparison:", "10" != 10)  
###########################################################################
#upper(): Converts all characters to uppercase.
message = "hello, world"
print("9. UpperCase:", message.upper())  

#lower(): Converts all characters to lowercase.
message = "HELLO, WORLD"
print("10. LowerCase:",message.lower())  

#strip(): Removes leading and trailing whitespace.
message = "   Hello, World!   "
print("11. Removed spaces:", message.strip())
print("11. Removed spaces:", message.rstrip())  

#replace(): Replaces one substring with another.
message = "Hello, World how are you!"
print("12. Replaced word:", message.replace("World", "Lee"))  

#find(): Finds the index of the first occurrence of a substring.
message = "Hello, World!"
print("13. The index of: ",message.find("World"))  

#split(): Splits a string into a list(Array) based on a delimiter.
message = "apple,banana,cherry"
print("14. splitted string:", message.split(","))  

