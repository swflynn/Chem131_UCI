import matplotlib.pyplot as plt        

# This script plots x,y data in a file seperated by a space

with open('data.dat') as f:             #open data file to plot
    lines = f.readlines()               # read in line by line (contains all lines)
    x = [line.split()[0] for line in lines]         #x = 1st number each line
    y = [line.split()[1] for line in lines]         #y = 2nd number each line

    plt.plot(x,y,label='PE(r) = 4e* [(s/r)^12 - (s/r)^6]')                       
    plt.xlabel('r')
    plt.ylabel('PE(r)')
    plt.title ('L-J-12-6 ')
    plt.legend()
    plt.savefig('L-J-12-6.png')                #save plot to a file
