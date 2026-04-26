import random

# 9-13. Dice
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))

print("6-sided die:")
die_6 = Die()
for _ in range(10):
    die_6.roll_die()

print("\n10-sided die:")
die_10 = Die(sides=10)
for _ in range(10):
    die_10.roll_die()

print("\n20-sided die:")
die_20 = Die(sides=20)
for _ in range(10):
    die_20.roll_die()

# 9-14. Lottery
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
winning_numbers = random.sample(lottery_pool, 4)
print(f"\nWinning lottery numbers: {winning_numbers}")
print("Any ticket matching these 4 numbers/letters wins a prize!")

# 9-15. Lottery Analysis
my_ticket = random.sample(lottery_pool, 4)
print(f"\nMy ticket: {my_ticket}")

attempts = 0
while True:
    attempts += 1
    drawn = random.sample(lottery_pool, 4)
    if drawn == my_ticket:
        break

print(f"It took {attempts} attempts to win!")

# 9-16. Python Module of the Week
# Visit https://pymotw.com to explore the Python standard library.
# The random module is a great starting point — it provides tools for
# generating random numbers, making random selections, and shuffling sequences.
