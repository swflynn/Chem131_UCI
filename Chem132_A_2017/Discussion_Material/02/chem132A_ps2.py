#====================================Welcome====================================#
#===============Here are my Python solution to Question 3 on PS2================#
#====================================Welcome====================================#

#==================================Importing Code===============================#
# The developers at Python have made code freely available that we can use.
# Numpy is a package that is useful for doing calculations.
# Use numpy arrays (lists of numbers) becuase they can be multiplied element-wise
#==================================Importing Code===============================#
import numpy as np                      # import numpy, call it np
import matplotlib.pyplot as plt
#==================================Importing Code===============================#

#================================Define Parameters==============================#
a=1.355              # vdw parameter for Argon, Bar-L^2 / mol^2
print ('The vdw a parameter for Argon is %r, (Bar-L^2/mol^2)')% a

b=0.03201             # vdw parameter for Argon, L / mol
print ('The vdw b parameter for Argon is %r, (L/mol)')% b

R=8.314                 # the gas constant J/(mol-K)
print ('The gas constant is %r, (J/mol-K)')% R
#================================Define Parameters==============================#

#===============================Populate Temperature============================#
#===================A List of numbers can easily be computed====================#
#==================Define the variable you want to be a list:===================#
T = np.arange(200,310,10)	
#=======Next choose a variable to append to the list (Temperature in this case)=#
#====================range(start_value,end_value,increment)=====================#
print ('The temperature\'s we will consider are: (K)')
print T
#print T[10] # this is the last element of T
#===============================Populate Temperature============================#

#============I will set V=1, P=1, n=1 and simplify all the equations============#
#=====================k_T = (1-B)^2 / (RT - 2a(1-B)^2)==========================#

#=========================Use the vdw EOS to Determine k_T======================#
k_T = []
for i in T:
	ans = (1-b)**2 / (R*i - 2*a*((1-b)**2))
        k_T.append(ans)
#=========================make k_T an array using asarray========================#
np.asarray(k_T)
print k_T
#=========================Use the vdw EOS to Determine k_T======================#

#=========Next solve the arbitrary EOS for y, and use the vdw value of k_T======#
#=============================y = -(k_t / (RT)) + 1=============================#
y=np.array(len(k_T))                    # make the array, must be correct size
y= -(k_T / (R*T)) + 1                   # arrays will multiply element by element
print'Here are the values for our y parameter'
print y
#=========Next solve the arbitrary EOS for y, and use the vdw value of k_T======#

#=================================Plot the Data=================================#
plt.plot(T,k_T)
plt.xlabel('Temperature (K)')
plt.ylabel('vdw Isotherm Compressibility')
plt.savefig('vdw_plot.png')
plt.close()

#plt.ylim(.23,.25)
plt.plot(T,y)
plt.xlabel('Temperature (K)')
plt.ylabel('Fitting Parameter y')
plt.savefig('y_plot.png')
plt.close()
#=================================Plot the Data=================================#

# Note the y value we determine is essentially the same for all temperatures. 
# This would suggest that using this form of equation is reasonable.
# The paramater does not change, meaning it is ~ a constant.
# For various temperatures our parameter is able to reproduce the results from the vdw equ.
