import matplotlib.pyplot as plt        

# This script plots x,y data in a file seperated by a space

with open('data.dat') as f:             #open data file to plot
    lines = f.readlines()               # read in line by line
    x = [line.split()[0] for line in lines]         #x = 1st number
    y = [line.split()[1] for line in lines]         #y = 2nd number
    z = [line.split()[2] for line in lines]         #z = 3nd number
    a = [line.split()[3] for line in lines]         #z = 4nd number

    plt.plot(x,y, label='e^-x')                       # plot it
    plt.plot(x,z, label='x^10')                       
    plt.plot(x,a, label='e^^-x * x^10')                       
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title ('Integrand Gamma Function')
    plt.legend()
    plt.savefig('myfig.png')                #save plot to a file
