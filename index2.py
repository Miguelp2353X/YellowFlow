import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 30)
theta = np.linspace(-2*np.pi, 6*np.pi, 200)     

x, theta = np.meshgrid(x, theta, indexing="ij")

phi = (np.pi / 2) * np.exp(-theta / (8 * np.pi))    

X3 = x * np.sin(theta) * np.sin(phi)
Y3 = x * np.cos(theta) * np.sin(phi)
Z3 = x * np.cos(phi)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X3, Y3, Z3, cmap="autumn")
plt.show()