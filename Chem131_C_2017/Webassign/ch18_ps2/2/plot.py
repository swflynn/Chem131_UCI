#See prob2.f90 for the data generation
#Our data file has 3 columns J, f(J) at 300K and f(J) at 1000K
# We want to make 2 plots to compare the distributions 

#======================Tell Python to let us make a Graph======================!
import matplotlib.pyplot as plt        


with open('data.dat') as f:             #open data file to plot
    lines = f.readlines()               # read in line by line
    x = [line.split()[0] for line in lines]         #x = 1st number
    y = [line.split()[1] for line in lines]         #y = 2nd number
    z = [line.split()[2] for line in lines]         #z = 3rd number

    plt.plot(x,y, label='300K')                       # plot it 300K
    plt.plot(x,z, label='1000K')                       # plot it 1000K
    plt.xlabel('J')
    plt.ylabel('f(J)')
    plt.title ('Webassign(2) Ch.18 #2')
    plt.legend()
    plt.savefig('myfig.png')                          #save plot to a file
