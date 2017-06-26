# Comments in Python are made using # character
# See 18_9_soln.f90 for the Fortran Code that generated the data. 

# This is a python program to take our data in data.dat and plot it. 
# Our data file has 2 columns T and C_v seperated by a space

#======================Tell Python to let us make a Graph======================!
import matplotlib.pyplot as plt     # Python Package for Plotting Data 

with open('data.dat') as f:         #open data file to read in data to Python
    lines = f.readlines()           # read in the data line by line
    x = [line.split()[0] for line in lines]         #x = 1st number [T]
    y = [line.split()[1] for line in lines]         #y = 2nd number [C(T)]

#===========================Plot the Data===========================!
    plt.plot(x,y)                       
    plt.xlabel('T(K)')
    plt.ylabel('C_v / R')
    plt.title ('McQuarre 18-9 Solution')
    plt.savefig('myfig.png')                #save plot to a file myfig.png
