print("\n <----------------- 8.3 ------------------->\n")
# 8-3. T-Shirt


def make_shirt(size, message):
    print(f"The shirt size is {size} and the message is: '{message}'")


# Positional arguments
make_shirt("Large", "I love Python")

# Keyword arguments
make_shirt(message="Keep Calm and Code On", size="Medium")
# Notice that the position of arguments does not matter when using keyword arguments


print("\n <----------------- 8.4 ------------------->\n")
# 8-4. Large Shirts


def make_shirt(size="Large", message="I love Python"):
    print(f"The shirt size is {size} and the message is: '{message}'")


make_shirt()                                      # large shirt, default message
# medium shirt, default message
make_shirt(size="Medium")
make_shirt(size="Small", message="Python Rocks")  # any size, different message


print("\n <----------------- 8.5 ------------------->\n")
# 8-5. Cities


def describe_city(city, country="Iceland"):
    print(f"{city} is in {country}.")


describe_city("Reykjavik")
describe_city("Berlin", "Germany")
describe_city("Tokyo", "Japan")
