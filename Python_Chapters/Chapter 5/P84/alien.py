# 5-3 Alien Colors #1 - Version that passes (green)
alien_color = 'green'
if alien_color == 'green':
    print("The player just earned 5 points.")

print('='*40)

# 5-3 Version that fails (no output)
alien_color = 'yellow'
if alien_color == 'green':
    print("The player just earned 5 points.")
# ^^ nothing with happen in output because condition is False

print('='*40)

# 5-4 Alien Colors #2 - Runs if block (green)
alien_color = 'green'
if alien_color == 'green':
    print("The player just earned 5 points for shooting the alien.")
else:
    print("The player just earned 10 points.")

print('='*40)

# 5-4 Runs else block (yellow)
alien_color = 'yellow'
if alien_color == 'green':
    print("The player just earned 5 points for shooting the alien.")
else:
    print("The player just earned 10 points.")

print('='*40)

# 5-5 Alien Colors #3 - Green
alien_color = 'green'
if alien_color == 'green':
    print("The player earned 5 points.")
elif alien_color == 'yellow':
    print("The player earned 10 points.")
else:
    print("The player earned 15 points.")

print('='*40)

# 5-5 Yellow
alien_color = 'yellow'
if alien_color == 'green':
    print("The player earned 5 points.")
elif alien_color == 'yellow':
    print("The player earned 10 points.")
else:
    print("The player earned 15 points.")

print('='*40)

# 5-5 Red
alien_color = 'red'
if alien_color == 'green':
    print("The player earned 5 points.")
elif alien_color == 'yellow':
    print("The player earned 10 points.")
else:
    print("The player earned 15 points.")

print('='*40)

# 5-6 Stages of Life
age = 1  # Change this value to test different stages
if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

print('='*40)

# 5-7 Favorite Fruit
favorite_fruits = ['bananas', 'apples', 'oranges']

if 'bananas' in favorite_fruits:
    print("You really like bananas!")

if 'apples' in favorite_fruits:
    print("You really like apples!")

if 'kiwi' in favorite_fruits:
    print("You really like kiwis!")

if 'oranges' in favorite_fruits:
    print("You really like oranges!")

if 'grapes' in favorite_fruits:
    print("You really like grapes!")
