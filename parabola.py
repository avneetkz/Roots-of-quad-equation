
# importing the required module
import matplotlib.pyplot as plt
import numpy as np

# x axis values
x = np.linspace(-10, 15)

# corresponding y axis values
y = x**2 - 5*x - 14

# plotting the points
plt.hlines(y=0, xmin=min(x), xmax=max(x), linestyles='dashed')
plt.vlines(x=0, ymin=min(y), ymax=max(y), linestyles='dashed')

# naming the x axis
plt.xlabel('x')

# naming the y axis
plt.ylabel('y')

# giving a title to my graph
plt.title('Roots of Quadratic equations')

plt.plot(x, y)

# function to show the plot
plt.show()
