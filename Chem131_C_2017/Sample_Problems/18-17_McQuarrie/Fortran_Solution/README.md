# Fortran Soltuion:
Here is a simple Fortran 90 Program to plot J and f(J) at 300 and 1000 K.

### 18_17_soln.f90:
The fortran program.
This file uses the Fortran Programming Language to calculate J and f(J). 
The output of this program is a data file; data.dat (with 3 columns).

### data.dat:
Data file containing 3 columns: J and f(300K), and f(1000K)

### plot.py:
Fortran cannot plot data by itself, this is a Python Program to open data.dat and plot it

### myfig.png:
This is the final result, a graph of J vs f(J)
