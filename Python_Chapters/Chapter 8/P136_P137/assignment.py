# 8-3. T-Shirt
def make_shirt(size, message):
    print(f"The shirt size is {size} and the message is: '{message}'")

# Positional arguments
make_shirt("Large", "I love Python")

# Keyword arguments
make_shirt(size="Medium", message="Keep Calm and Code On")

# 8-4. Large Shirts
def make_shirt(size="Large", message="I love Python"):
    print(f"The shirt size is {size} and the message is: '{message}'")

make_shirt()                                      # large shirt, default message
make_shirt(size="Medium")                         # medium shirt, default message
make_shirt(size="Small", message="Python Rocks")  # any size, different message

# 8-5. Cities
def describe_city(city, country="Iceland"):
    print(f"{city} is in {country}.")

describe_city("Reykjavik")
describe_city("Berlin", "Germany")
describe_city("Tokyo", "Japan")
