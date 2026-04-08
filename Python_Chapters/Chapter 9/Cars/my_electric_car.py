from electric_car import ElectricCar

my_ford_ranger = ElectricCar('ford', 'ranger', 2024)
print(my_ford_ranger.get_descriptive_name())

my_ford_ranger.battery.describe_battery()
my_ford_ranger.battery.get_range()