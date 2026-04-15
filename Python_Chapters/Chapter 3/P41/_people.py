# 3.4 Guest List:
guests = ["Noah", "Leonardo", "Randy", "Omen", "Samara"]
print(guests, "\n")

# 3.5 Changing Guest List:
# Randy will be absent so we'll replace him with Ruth
guests[2] = "Ruth"
print(guests, "\n")

# 3.6 More Guests:
guests.insert(0, "Lodi")
guests.insert(3, "Love")
guests.insert(1, "Joyce")
print(guests, "\n")

# 3.7 Shrinking Guest List:
_1st_pop = guests.pop()
print(f"\nI'm so sorry {_1st_pop}, my daughter said you can't come")

_2nd_pop = guests.pop()
print(f"\nAy, {_2nd_pop} we changed our mind, we'll invite you to our cookout instead.")

_3rd_pop = guests.pop()
print(f"\nButhi {_3rd_pop}, the other time my friend said you were drinking too much, so you are not invited again. Sorry!!")

_4th_pop = guests.pop()
print(f"\n{_4th_pop}, can we invite you another time, we have an emergency travel")

_5th_pop = guests.pop()
print(f"\nAs for {_5th_pop}, we just don't have a reason to not invite you, we'll find something special to do instead")

_6th_pop = guests.pop()
print(f"\nOh {_6th_pop}, we canceled you invitation because we just remembered you had to go to Italy for you tennis match")

# remaining 2 guests
print(f"{guests[0]}, You are still invited")
print(f"Congratulations {guests[1]}, We'll come a pick you up for dinner")

# deleting the last two
del guests[1]
del guests[0]
print(guests)

# 3.9 Dinner Guests;
print(f"There are only {len(guests)} guest remaining.")
