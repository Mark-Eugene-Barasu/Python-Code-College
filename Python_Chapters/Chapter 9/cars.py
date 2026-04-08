class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make  
        self.model = model  
        self.year = year  
        self.odometer_reading = 0   # Initial mileage is set to 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"  
        return long_name.title()    # Return the name with proper capitalization

    def read_odometer(self):
        """Print a statement showing the current car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")  

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading: # Ensure mileage is not less than current reading
            self.odometer_reading = mileage  # Update the mileage
        else:
            print("You can't roll back an odometer!")  # Prevent rolling back the odometer

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles  # Increment the mileage by the specified number of miles


# Example of creating a different car and using the methods

my_used_car = Car('toyota', 'corolla', 2015)# Create a new used car instance
print(my_used_car.get_descriptive_name())   # Displays the car's name

my_used_car.update_odometer(45_000)         # Set the initial mileage to 45,000 miles
my_used_car.read_odometer()                 # Displays the current mileage of the used car

my_used_car.increment_odometer(200)         # Add 200 miles to the odometer
my_used_car.read_odometer()                 # Displays the updated mileage after incrementing

