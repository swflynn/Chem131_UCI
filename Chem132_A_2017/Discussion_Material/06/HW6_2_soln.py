from math import pow        # Powers of a Number
import numpy as np          # Better Math tools

n = 10 / (6.02*pow(10,23))  # number of moles (via avogadro's number)
V = 1*pow(10,-3)            # Volume
Vm = V/n                    # Molar Volume
print('This is the Molar Volume: %s')% Vm

B = -0.141                  # Virial Coef
R = 0.082                   # Gas Constant
T = 2.7                     # Temperature
M = 4.003*pow(10,-3)                  # Mass Helium
P1 = R*T/Vm                 # Ideal Gas Pressure
P1 = P1*760                 # Convert to Torr
print('This is the Ideal Pressure (Torr): %s') % P1

P2 = (R*T/Vm)* (1+ (B/Vm))  # Pressure Virial
P2 = P2*760                 # pressure to torr
print('This is the Virial Pressure(Torr): %s') % P2

R2 = 8.314                  # other gas constant units

V_mp = np.sqrt(2*R2*T / M)           # Most Probable Speed
print('This is the Most Probable Speed: %s')% V_mp

V_ave = np.sqrt(8*R2*T / (M*np.pi))          # Average Speed
print('This is the Average Speed: %s')% V_ave

V_rms = np.sqrt(3*R2*T/M)            # Root-Mean Squared
print('This is the Root-Mean Square Speed: %s')% V_rms


d=258*pow(10,-12)                   # helium collision diameter)
sigma = np.pi*d**2
P3 = P2 * 1.01325*pow(10,5) / 760
k = 1.38065*pow(10,-23)             # boltzmann constant
lambd = k*T/(sigma*P3)

print('The average distance before a collision is: %s') % lambd
