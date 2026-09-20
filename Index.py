import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 70)
theta = np.linspace(-2*np.pi, 15*np.pi, 700)   

x, theta = np.meshgrid(x, theta, indexing="ij")

phi = (np.pi / 2) * np.exp(-theta / (8 * np.pi))

y = 1.95653 * x**2 * (1.27689 * x - 1)**2 * np.sin(phi)

r  = x * np.sin(phi) + y * np.cos(phi)
Z3 = x * np.cos(phi) - y * np.sin(phi)

u = np.mod(3.6 * theta, 2*np.pi) / np.pi   
X = 1 - 0.5 * ((5/4) * (1 - u)**2 - 1/4)**2

r  = X * r
Z3 = X * Z3

X3 = r * np.sin(theta)
Y3 = r * np.cos(theta)

fig = plt.figure(figsize=(8,8), facecolor="black")
ax = fig.add_subplot(111, projection="3d", facecolor="black")
ax.plot_surface(X3, Y3, Z3, cmap="autumn", edgecolor=(1,0.75,0.1), linewidth=0.1, alpha=0.95)
ax.set_axis_off()
ax.view_init(elev=30, azim=30)
plt.show()