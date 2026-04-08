#1. Define a class called Dog:
class Dog:
    """A simple attempt to model a dog."""
    
    # The __init__ method is the constructor that gets called when we create an instance of Dog
    def __init__(self, name, age):
        """Initialize name and age attributes for the dog."""
        self.name = name  # Assign the given 'name' to the instance's 'name' attribute
        self.age = age    # Assign the given 'age' to the instance's 'age' attribute

    # Method that shows a dog sitting
    def sit(self):
        print(f"{self.name} is now sitting.")  

    # Method that shows a dog rolling over
    def roll_over(self):
        print(f"{self.name} rolled over!")  

#2. Creating an Instance:
my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Add a blank line between age and calling methods
print()  # This will add space

#3. Accessing attributes with dot notation
print(my_dog.name)  
print(my_dog.age)   

# Add a blank line between age and calling methods
print()  # This will add space

#4. Calling Methods from the Dog class:
my_dog.sit()  
my_dog.roll_over()

#5. Creating Multiple Instances:
my_dog = Dog('Rex', 1)
your_dog = Dog('Lucy', 3)

print(f"\nMy dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
