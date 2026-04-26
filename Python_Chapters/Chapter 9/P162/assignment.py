# 9-1. Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("The Italian Place", "Italian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2. Three Restaurants
restaurant1 = Restaurant("Sushi World", "Japanese")
restaurant2 = Restaurant("Burger Barn", "American")
restaurant3 = Restaurant("Spice Garden", "Indian")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# 9-3. Users
class User:
    def __init__(self, first_name, last_name, age, city, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.hobby = hobby

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}, Age: {self.age}, City: {self.city}, Hobby: {self.hobby}")

    def greet_user(self):
        print(f"Welcome back, {self.first_name} {self.last_name}!")

user1 = User("John", "Doe", 30, "Berlin", "cycling")
user2 = User("Jane", "Smith", 25, "London", "painting")
user3 = User("Mark", "Jones", 35, "New York", "coding")

for user in [user1, user2, user3]:
    user.describe_user()
    user.greet_user()
