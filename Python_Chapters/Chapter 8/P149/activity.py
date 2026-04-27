# 8-12. Sandwiches
print("< ------------------- 8-12. Sandwiches ------------------ >")
def make_sandwich(*items):
    print("\nMaking a sandwich with:")
    for item in items:
        print(f" {items.index(item) + 1}. {item}")

make_sandwich("turkey")
make_sandwich("ham", "cheese")
make_sandwich("tuna", "lettuce", "tomato", "mayo")

# 8-13. User Profile
print("\n\n< ------------------- 8-13. User Profile ------------------ >")
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

profile = build_profile("Mark", "Smith",
                        age=25,
                        city="Berlin",
                        hobby="coding")
print(f"\n{profile}")

# 8-14. Cars
print("\n\n< ------------------- 8-14. Cars ------------------ >")
def make_car(manufacturer, model, **options):
    car = {'manufacturer': manufacturer, 'model': model}
    car.update(options)
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(f"\n{car}")
