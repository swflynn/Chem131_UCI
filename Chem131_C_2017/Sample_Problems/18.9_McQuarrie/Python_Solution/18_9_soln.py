# This is a Python 2 program (.py).
# Comments are specified with the # caracter and are not part of the code

#====================================Question=======================================#
# Plot the vibrational contribution to molar heat capcity of Br2(g) from (250-1000)K
#====================================Question=======================================!

#====================================Solution=======================================!
# From P.741 of McQuarrie : C = R(O/T)^2 (e^-o/T / (1-e^-o/T)^2)
#====================================Solution=======================================!

#====================================Program=======================================!
# Simple program to calculate C/R as a function of T from 250-1000 K
# The data is written to a file data.dat
# See plot.py Python code for plotting this data file
#====================================Program=======================================!

# Begin The Program
import numpy as np                  # Python Package for 'better' math
import matplotlib.pyplot as plt     # Python Package for Graphing

vib_temp = 463.                     # McQuarrie P. 739

# Make a numpy array (np.) aka a vector for the temperature
T = np.arange(250.,1000.,1.)        # Temperature from 250-1000 increase by 1

# Because C_v depends on T, Python will make is a numpy array too
C_v = (vib_temp / T)**2 * ((np.exp(-(vib_temp / T))) / ((1. - np.exp(-(vib_temp / T)))**2))

#===========================Plot the Data===========================!
plt.plot(T,C_v)                       
plt.xlabel('T(K)')
plt.ylabel('C_v / R')
plt.title ('McQuarrie 18-9 Solution')
plt.savefig('myfig.png')                #save plot to a file myfig.png
