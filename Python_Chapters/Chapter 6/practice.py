people = [
    {"name": "John", "age": 30, "city": "Berlin"},
    {"name": "Jane", "age": 25, "city": "London"},
    {"name": "Mark", "age": 35, "city": "New York"}
]

for person in people:
    print(f'{person["name"]} is {person["age"]} of age and lives in {person["city"]}')
