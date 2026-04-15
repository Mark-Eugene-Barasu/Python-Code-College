places = ["Durban", "Cape Town", "Manhattan", "Brooklyn", "Port-Alfred"]
print(places)
print(sorted(places))
print(places)

places.reverse()
print(places)

places.reverse()
print(places)

places.sort()
print(places)

# 3.10 Every Function
languages = ["English", "French", "Spanish", "Greek", "Twi", "Dutch", "Latin"]
print("\n", languages)

languages[1] = "Xhosa"  # replacing the 2nd language
print("\n", languages)

# check through and remove 1st Dutch if only it is there
languages.remove("Dutch")
print("\n", languages)

del languages[-1]  # delete last language
print("\n", languages)

languages.sort()  # arranges languages alphabetically
print("\n", languages)

languages.reverse()  # this reverse the alphabetically sorted list of languages
print("\n", languages)

print(sorted(languages))
""" the sorted() function sorts the languages out without changing the original order of the list
"""
