# McQuarrie; Problem 18-9 (Page 757)

## Problem:
Plot the vibrational Contribution to the Molar Heat Capacity from (250-1000)K for a diatomic gas.

## Answer:
Using equation 18.26 (P.741) we find C_vib(T) for diatomic molecules. 

## Code:
I have written two different programs to solve this problem, one in Fortran and the other in Python. 
The solutions are the same, this is simply as example of how different programming languages look. 

### Fortran Solution:
To solve this problem I have written a simple Fortran program to calculate T and C(T) for a given temperature range. 
Fortran is not able to plot data internally, so I write the results to a data file (data.dat).
I then use a simple Python Program to open the data file and plot the data. 

### Python Solution:
To solve this problem I have written a simple Python program to calculate T and C(T) and then plot the data (this is all done using 1 python program). 
