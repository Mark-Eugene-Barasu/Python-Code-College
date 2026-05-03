import json
import os

# Chapter 10 Exercises 10-11 to 10-14 COMPLETE implementation
# JSON persistence for favorite number and user info
# Files in P206 dir. Descriptive comments on every line/block.

print('=== 10-11/10-12 Favorite Number ===')


def get_stored_number(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)  # Load stored number
    return None  # No file, return None


def store_new_number(filename):
    number_str = input('Favorite number? ')
    try:
        number = int(number_str)
        with open(filename, 'w') as f:
            json.dump(number, f)  # Store as JSON
        print(f'Stored your favorite number: {number}')
        return number
    except ValueError:
        print('Invalid number - try again.')
        return store_new_number(filename)  # Recurse on error


filename_num = './favorite_number.json'
num = get_stored_number(filename_num)
if num:
    print(f'I remember your favorite number is {num}!')
else:
    store_new_number(filename_num)

print('\\n=== 10-13/10-14 User Dict Verification ===')


def get_stored_user(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return None


def get_user_info(filename):
    user = {}
    user['username'] = input('Username: ')
    user['favorite_color'] = input('Favorite color: ')
    user['hobby'] = input('Hobby: ')
    with open(filename, 'w') as f:
        json.dump(user, f)
    print(
        f'Stored info for {user["username"]}: color={user["favorite_color"]}, hobby={user["hobby"]}')
    return user


def verify_user_info(filename):
    data = get_stored_user(filename)
    if not data:
        return get_user_info(filename)
    print(f'Is {data["username"]} correct? (y/n): ', end='')
    if input().lower() != 'y':
        print('Updating info...')
        return get_user_info(filename)
    print(f'Remember: color={data["favorite_color"]}, hobby={data["hobby"]}')


filename_user = './user_info.json'
verify_user_info(filename_user)

print('Done - files in P206/')
