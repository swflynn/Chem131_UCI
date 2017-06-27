# Here is a quick Python solution to Problem 1 on the Mixing Addition Problem Set

import numpy as np      # convenient for doing math

P_1 = 10.               # Initial pressure Oxygen (atm)
V_o = 1.                # Initial Volume Oxygen (L)
T = 298.                # Temperature  (K)
P_2 = 1.                # Initial Pressure Nitrogen (atm)
V_n = 1000.             # Initial Volume Nitrogen (L)
R_n = 0.0820573         # Gas Constant (L-atm / mol-K)
R = 8.314               # Gas Constant (J/mol-K)

# Calulate moles of Oxygen (Ideal Gas Law)
n_o = P_1*V_o / (R_n*T)
print('The moles of O_2 are')
print(n_o)

# Calculate moles of Nitrogen (Ideal Gas Law)
n_n = P_2*V_n / (R_n*T)
print('The moles of N_2 are')
print(n_n)

# The system is closed therefore
n_tot = n_o + n_n
print('There are %s total moles in the system') %n_tot

# The system is composed of gases therefore
V_tot = V_o + V_n

# The system is ideal, so the partial pressures are determined without interactions
P_o = n_o*R_n*T / V_tot
P_n = n_n*R_n*T / V_tot
print('The partial pressure of oxygen is %s and nitrogen is %s')%(P_o,P_n)

# Gibbs Free Energy Equation 
G = n_o * R * T * np.log(P_o/P_1) + n_n * R * T * np.log(P_n/P_2)

# The system is ideal therefore Enthalpy = 0 and 
S = -G / T

print('The change in the Gibbs is %s')%G
print('The change in the Entropy is %s')%S
