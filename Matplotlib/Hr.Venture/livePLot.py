import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(80, 180, 200)
y = np.random.randint(80, 180, 200)
z = np.random.randint(80, 180, 200)

X = []
Y = []
Z = []
for index in range(x.shape[0]):
    axes = plt.axes(projection='3d')
    X.append(x[index])
    Y.append(y[index])
    Z.append(z[index])
    axes.scatter3D(X,Y,Z)
    plt.pause(0.1)
plt.show()