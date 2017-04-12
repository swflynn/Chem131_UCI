Solution to a problem similar to McQuarrie 18.17

Question:
Plot the fraction of HBr molecules in various rotational levels at both 300K and 1000K (consider J from 0 to 50). 

Answer:
From P.745 McQuarrie (EQU.18.35) we find a fraction of diatomic molecules as a function of J.

Code:

prob2.f90 : Fortran code to calculate and write J, f(J) 300K, f(J) 1000K to a file.

data.dat : Data file with 3 columns J    f(J) at 300K    f(J) at 1000K

plot.py : Python code to plot our data, reads in data.dat and outputs myfig.png

myfig.png : The final answer!!!

a.out : This is machine code written by the fortran compiler, !===IGNORE THIS FILE===!

.DS_Store : This is a github maitenance file, !===IGNORE THIS FILE===!
