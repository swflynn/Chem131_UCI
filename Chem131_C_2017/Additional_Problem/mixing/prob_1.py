# Here is a quick python solution to Problem 1 on the Mixing Addition Problem
# Mac has python software as part of the factory set-up simply open a termianl to this file
# Once in the same directory as this file type: python prob_1.py
# A tank of volume 1 liter filled with O2 gas at a temperature of T=298K and pressure of
# p=10atm.is attached to a vessel of volume V =1m3 full of N2 gas at T=298K and 
# p= 1 atm. The valve is opened and the gases are allowed to mix. Assuming they are ideal
# Calculate the change in Gibbs Free Eenrgy and Entropy

import numpy as np

P_1 = 10.               # Initial pressure Oxygen
V_o = 1.                # Initial Volume Oxygen
T = 298.                # Initial Temperature Oxygen
P_2 = 1.                # Initial Pressure Nitrogen
V_n = 1000.             # Initial Volume Nitrogen
R_n = 0.0820573         # Gas Constant L-atm / mol-K
R = 8.314               # Gas Constant J/mol-K

n_o = P_1*V_o / (R_n*T)
print('The moles of O_2 are')
print(n_o)
n_n = P_2*V_n / (R_n*T)
print('The moles of N_2 are')
print(n_n)

n_tot = n_o + n_n
print('There are %s total moles in the system') %n_tot

V_tot = V_o + V_n

P_o = n_o*R_n*T / V_tot
P_n = n_n*R_n*T / V_tot

print('The partial pressure of oxygen is %s and nitrogen is %s')%(P_o,P_n)


G = n_o * R * T * np.log(P_o/P_1) + n_n * R * T * np.log(P_n/P_2)

S = -G / T

print('The change in the Gibbs is %s')%G
print('The change in the Entropy is %s')%S
