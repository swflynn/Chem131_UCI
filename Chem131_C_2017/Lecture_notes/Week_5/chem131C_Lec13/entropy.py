#May 2017, Lecture 13 notes
#plot ln (x) and x - 1 from 1 to 5
#If you have python 2 on your computer simply type $ python test.py to run the code

import numpy as np                      #Package for more math tools
import matplotlib.pyplot as plt         #Package for Plotting


x = np.arange(1.,5.,.1)                 #list of values from 1 to 5 (0.1 increment)
y = x - 1
z = np.log(x)                           #np calls numpy package, log = ln

plt.plot(x,y, color='r', label='x-1')                       
plt.plot(x,z, color='b', label='ln(x)')     #plt calls the pyplot package above 
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title ('Entropy of the Universe')
plt.legend()
plt.savefig('myfig.png') 
