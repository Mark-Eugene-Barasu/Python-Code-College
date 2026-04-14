bicycles = ["trek", "cannondale", "redline", "specialized"]
print(type(bicycles), "\n")
print(bicycles, "\n")

for x in bicycles:
    if bicycles.index(x) == 2:
        continue
    print(f"{x} is at index number: {bicycles.index(x)}", "\n")