new_dict = {
    "id": 1,
    "name": "John",
    "age": 30,
    "city": "Berlin"
}

for key, value in new_dict.items():
    if type(value) == str:
        print(key, value.upper())
    else:
        del key
        del value
    print(new_dict)