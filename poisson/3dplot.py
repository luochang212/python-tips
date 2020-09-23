import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


def calculator(upsilon, k):
    """upsilon = rate * t"""
    return upsilon ** k / np.math.factorial(k) * np.exp(-upsilon)


x = np.linspace(1, 30, 30)
z = np.array([[calculator(i, j) for i in x] for j in x])
x, y = np.meshgrid(x, x)


fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot_surface(x, y, z, cmap=cm.gray)
plt.show()
