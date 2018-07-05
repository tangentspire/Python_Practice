import matplotlib.pyplot as plt

x_values = range(1, 1000)
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues)

plt.show()
