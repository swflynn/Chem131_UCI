# McQuarrie; Problem 18-9 (Page 758)

## Problem:
Plot the fraction of HBr molecules in various rotational levels at both 300K and 1000K (consider J from 0 to 50). 

## Answer:
From P.745 McQuarrie (EQU.18.35) we find a fraction of diatomic molecules as a function of J.

## Code:
I have written two different programs to solve this problem, one in Fortran and the other in Python. 
The solutions are the same.
This is simply as example of how different programming languages look. 

### Fortran Solution:
To solve this problem I have written a simple Fortran program to calculate J and f(J) for both T=300K and 1000K. 
Fortran is not able to plot data internally, so I write the results to a data file (data.dat).
I then use a simple Python Program to open the data file and plot the data. 

### Python Solution:
To solve this problem I have written a simple Python program to calculate J and f(J) at both 300K and 1000K.
Then I plot the data and save the figure. 
