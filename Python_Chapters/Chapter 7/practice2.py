
used_colors = ['blue', 'black', 'red', 'green', 'orange']
confirmed_colors = []

while used_colors:
    current_color = used_colors.pop()  # Remove last color from the list
    print(f"Verifying color: {current_color.title()}")
    confirmed_colors.append(current_color)  # Add to the confirmed colors list

print("\nThe following colors have been confirmed:")
for confirmed_color in confirmed_colors:
    print(f" - {confirmed_color.title()}")


print(used_colors)
print(confirmed_colors)
