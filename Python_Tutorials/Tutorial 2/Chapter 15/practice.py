from matplotlib import pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.plot(input_values, squares)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value (x axis)", fontsize=14)  
plt.ylabel("Square of Value (y axis)", fontsize=14)
plt.tick_params(labelsize=14)
plt.show()
