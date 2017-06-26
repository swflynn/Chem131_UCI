# McQuarrie; Problem 18-9 (Page 757)

## Problem:
Plot the vibrational Contribution to the Molar Heat Capacity from (250-1000)K for a diatomic gas.

## Answer:
Using equation 18.26 (P.741) we find C_vib(T) for diatomic molecules. 

## Code:
I have written two different programs to solve this problem, one in Fortran and the other in Python. 
The solutions are the same, this is simply as example of how different programming languages look. 

### Fortran Solution:

To solve this problem I have written a simple Fortran program (fortran_soln.f90).
The program calculates T and C(T) for a given range. 
Fortran is not able to plot data internally, so I write the results to a data file (data.dat).
I then wrote a simple Python program to open the data file and plot the data. 

#### fortran_soln.f90
Fortran code to calculate and write T, C(T) to a file

data.dat : Data file with 2 columns T, C(T)

plot.py : Python code to plot our data, reads in data.dat and outputs myfig.png

myfig.png : The final answer!!!

a.out : This is machine code written by the fortran compiler, !===IGNORE THIS===!

.DS_Store : This is a github maitenance file, !===IGNORE THIS===!



### Python Solution:

