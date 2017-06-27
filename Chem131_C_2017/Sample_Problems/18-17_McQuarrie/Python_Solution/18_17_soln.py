# This is a Python 2 program (.py).
# This problem is similar to Problem 18-17 in McQuarrie. 

#====================================Question======================================#
# Plot the fraction of HBr(g) molecules in various rotation levels (J=0,50)
# Compare T = 300k and T = 1000K population distributions
#====================================Question======================================#

#====================================Solution======================================#
# From P.745 of McQuarrie : f(J) = (2J+1) (o/T) (e^-o*J(J+1)/T)
# Expect at higher Temperature we have more energy, therefore higher J states 
# Have a higher probability of being populated. 
#====================================Solution======================================#

#====================================Program=======================================#
# Set our indepedent variable J (quantum number) from 0-50: (j)
# Solve for population density at 300K: (f)
# Solve for population density at 1000K: (g)
# Write data to a file for plotting in Python
#====================================Program=======================================#

# Begin The Program
import numpy as np                  # Python Package for 'better' math
import matplotlib.pyplot as plt     # Python Package for Graphing

rot_temp = 12.02                     # McQuarrie P. 739
T1 = 300                            # temperature for analysis (K)
T2 = 1000

# Make a numpy array (np.) aka a vector for the quantum state
J = np.arange(0.,51.,1.)        # Quantum State from 0to 50, increase by 1

# Because f depends on J, Python will make is a numpy array too
f_1 = (2.*J +1.) * (rot_temp / T1) * (np.exp(-(rot_temp*J*(J+1))/T1))   #T=300

f_2 = (2.*J +1.) * (rot_temp / T2) * (np.exp(-(rot_temp*J*(J+1))/T2))   #T=1000

#===========================Plot the Data===========================!
plt.plot(J,f_1, label='300K')                       # plot it 300K
plt.plot(J,f_2, label='1000K')                       # plot it 1000K
plt.xlabel('J')
plt.ylabel('f(J)')
plt.title ('McQuarrie 18-17 Solution')
plt.legend()
plt.savefig('myfig.png')                          #save plot to a file
