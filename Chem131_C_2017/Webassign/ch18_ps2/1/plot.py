import matplotlib.pyplot as plt        

# This script plots x,y data in a file seperated by a space

with open('data.dat') as f:             #open data file to plot
    lines = f.readlines()               # read in line by line
    x = [line.split()[0] for line in lines]         #x = 1st number
    y = [line.split()[1] for line in lines]         #y = 2nd number

    plt.plot(x,y)                       # plot it
    plt.xlabel('T(K)')
    plt.ylabel('C_v / R')
    plt.title ('Webassign(2) Ch.18 #1')
    plt.savefig('myfig.png')                          #save plot to a file
