# Mixing Problem:
Quick Python calculation for the additional problem 1 from the mixing assignment.

## Question:
A tank filled with O2 gas at a temperature of T = 298(K) and pressure of p = 10 (atm) is attached to a vessel of volume V = 1(m3) full of N2 gas at T = 298(K) and p = 1(atm) pressure.
The valve is opened and the gases are allowed to mix. 
Assuming they are both ideal diatomic gases (C_v = 5/2 R) , calculate the change in Gibbs free energy and entropy of the process.

## Solution:
The system is ideal, we can determine the number of moles for each component with the ideal gas law. 

The system is closed, therefore we can determine the total number of moles as the sum of Oxygen and Nitrogen moles. 

The gases are ideal therefore the partial pressure is determined indepedent of the other gas. 

Gibbs Free Energy is calcualted with G = sum_i n_i mu_i (moles and chemical potentials

The chemical potential for an ideal gas mixture can be simplified as 
mu = mu_ref + RT ln(p_i / p_ref)

Finally the enthalpy of mixing is 0 for an ideal solution by definition therefore
G = -T delta S
