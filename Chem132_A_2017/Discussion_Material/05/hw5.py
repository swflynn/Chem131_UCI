import numpy as np                      # Better Numbers and Arrays
import matplotlib.pyplot as plt         # Graphing with Python

K = np.array([1.32, 0.47, 0.21, 0.1])   # Equilibrium Constant
T = np.array([900, 1000, 1100, 1200])    # Temperature array (Kelvin)

# We need to plot ln K v 1/T, the slope of this line times R Gives the Enthalpy of Reaction. 
lnK = np.log(K)
iT = 1./T

# Numpy Polynomial fit to get Slope
slope, intercept = np.polyfit(iT, lnK, 1)
print('This is your slope: %s') % slope
H = slope* 8.314/ 1000
print('This is your Enthalpy (kJ/mol) %s') % H               # Units are kJ/mol

plt.plot(iT, lnK)
plt.xlabel('1/Temperature')
plt.ylabel('ln K')
plt.show()

