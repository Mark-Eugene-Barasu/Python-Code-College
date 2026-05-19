class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 1. Default value set automatically

    def update_odometer(self, mileage):
        """Set odometer, rejecting attempts to roll it back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


my_car = Car('Audi', 'A4', 2024)

# Method 1: Modifying directly
my_car.odometer_reading = 23

# Method 2: Modifying via a method (with built-in security logic)
my_car.update_odometer(35)

# Method 3: Incrementing the value
my_car.increment_odometer(100)

# Standalone class to be used for Composition
class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def get_range(self):
        if self.battery_size == 40:
            return 150
        elif self.battery_size == 65:
            return 225

# ElectricCar inherits from Car (Inheritance)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        # Initializes parent attributes (make, model, year, odometer)
        super().__init__(make, model, year)

        # Composition: Storing a Battery instance as an attribute
        self.battery = Battery()

    # Overriding: Replacing a parent method that doesn't apply to EVs
    def fill_gas_tank(self):
        print("This car doesn't have a gas tank!")


# Using the composed object
my_leaf = ElectricCar('Nissan', 'Leaf', 2024)
my_leaf.fill_gas_tank()  # Output: This car doesn't have a gas tank!

# Accessing the internal instance method using chained dot notation
# Output: Range: 150 miles.
print(f"Range: {my_leaf.battery.get_range()} miles.")
