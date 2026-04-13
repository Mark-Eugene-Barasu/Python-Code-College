
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# modify an element (replacing an existing element)
colors[0] = "black"
print(f"1. Modified colors list: {colors}", "\n")

colors[4] = "chartreuse"
print(f"2. Modified colors list: {colors}", "\n")


# using .append() to add to the END of a list
colors.append("while")
print(f"3. Appended(added) to the color list: {colors}", "\n")

colors.append("purple")
print(f"4. appended to my color list: {colors}", "\n")


# using .insert() to add to the BEGINNING of a list
colors.insert(0, "magenta")
print(f"5 Inserted {colors[0]} to the beginning of the list: {colors}", "\n")
