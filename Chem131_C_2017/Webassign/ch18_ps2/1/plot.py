# See prob1.f90 for the beginning of this problem.

# This is a python program to take our data in data.dat and plot it. 
# Our data file has 2 columns T and C_v

#======================Tell Python to let us make a Graph======================!
import matplotlib.pyplot as plt        

with open('data.dat') as f:         #open data file to get our numbers in python
    lines = f.readlines()           # read in the data line by line
    x = [line.split()[0] for line in lines]         #x = 1st number
    y = [line.split()[1] for line in lines]         #y = 2nd number

#===========================Plot the Data===========================!
    plt.plot(x,y)                       
    plt.xlabel('T(K)')
    plt.ylabel('C_v / R')
    plt.title ('Webassign(2) Ch.18 #1')
    plt.savefig('myfig.png')                #save plot to a file myfig.png
