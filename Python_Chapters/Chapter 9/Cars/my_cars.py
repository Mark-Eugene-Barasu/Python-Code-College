#Importing Multiple Classes from a Module
from electric_car import ElectricCar, Car

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
print()

############################################################
#Importing an Entire Module
import car
 
my_benz = car.Car('mercedes-benz', 's-class', 2024)
print(my_benz.get_descriptive_name())

my_benz.update_odometer(45_000)
my_benz.read_odometer()

my_benz.increment_odometer(200) 
my_benz.read_odometer()
print()

##########################################################
# Importing a Module into a Module
from car import Car  
from electric_car import ElectricCar  

# Creating an instance of the Car class
my_jaguar = Car('jaguar', 'xf', 2024)
print(my_jaguar.get_descriptive_name())

# Creating an instance of the ElectricCar class
my_bmw = ElectricCar('bmw', 'i4', 2024)
print(my_bmw.get_descriptive_name())
print()

########################################################
# Using Aliases
from electric_car import ElectricCar as EC  

# Creating an instance of the ElectricCar class using the alias
my_polo = EC('volkswagen', 'polo', 2024)
print(my_polo.get_descriptive_name())

