import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(80, 180, 50)
y = np.random.randint(80, 180, 50)
z = np.random.randint(80, 180, 50)
axes = plt.axes(projection='3d')
axes.scatter3D(x, y, z)
plt.show()