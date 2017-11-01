import numpy as np
import matplotlib.pyplot as plt

T = np.array([110.9, 112, 114, 115.8, 117.3, 119, 121.1, 123])
x = np.array([0.908, 0.795, 0.615, 0.527, 0.408, 0.300, 0.203, 0.097])
y = np.array([0.923, 0.836, 0.698, 0.624, 0.572, 0.410, 0.297, 0.164])

plt.plot(x, T, 'ro')
plt.plot(y,T, 'bo')
plt.ylabel('Temperature')
plt.xlabel('Mole Fraction')
plt.show()

