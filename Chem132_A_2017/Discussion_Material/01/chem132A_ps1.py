#====================================Welcome====================================#
#===============Here are my Python solution to Question 3 on PS1================#
#========================== This is the Python solution!========================#
#======Please Speak to Shane about Python, see Moises for the Mathematica code==#
#====================================Welcome====================================#

#==========================A few Comments About Python==========================#
#=====================Anything following a # symbol is a comment================#
#=========Comments are for the user, they do not do anything in the code========#
#=============I will use comments to explain everything in the program==========#
#==========================A few Comments About Python==========================#

#==================================Importing Code===============================#
# The developers at Python have made code freely available that we can use.
# Specifically the science-people have made packages such as numpy and scipy 
# Numpy essentially makes your number more accurate for calculations.
# Scipy is a package contianing various function for scientific computing
# You will need to download scipy to run this program, ask Google how to do this!
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#==================================Importing Code===============================#
import numpy as np                      # import numpy, call it np
from scipy.integrate import quad        # import 'quad' function form scipy
#=============================Define Our Integrand==============================#
# We need to tell python what function we want to integrate. 
# we 'define' our integrand (the thing inside the integral) as a function of x 
# for each value of x we return the integrand evaluated at that x
#=============================Define Our Integrand==============================#
M=0.018015              # the mass of water, kg/mol
print ('The mass of water is %r, (kg/mol)')% M
R=8.314                 # the gas constant J/(mol-K)
print ('The gas constant is %r, (J/mol-K)')% R
T=373.2                 # temperature in K
print ('The temperature of the gas is %r, (K)')% T
pie = np.pi             # the value of pi (3.14....), use numpy for accuracy
print ('The numerical value of pi is %r')% pie
coef = 4*pie*((M/(2*pie*R*T))**(1.5))           # terms that don't depend on v
# E is for our expectation value
def E(x):
    return  x * x**2 * np.exp(-((M*x**2)/(2*R*T)))
#=============================Compute Our Integral==============================#
# Now that we have defined our integrand we can compute our integral
# We do this by using the quad function from scipy, which does numerical integration
# the answer we get from quad is exp_x (err = the numerical error)
#=============================Compute Our Integral==============================#
exp_x, err  = quad(E,0,np.infty)
exp_x = exp_x*coef
print ('The expectation value (average value) for the speed of our water vapour is')
print exp_x, 'm/s'
#=============================The Variance Integral=============================#
# Now that we have the expectation value we can compute the variance 
#=============================The Variance Integral=============================#
def Var(x):
    return (x-exp_x)**2 * x**2 * np.exp(-((M*x**2)/(2*R*T)))

var_x, err = quad(Var,0,np.infty)
var_x = var_x*coef
print ('The variance in the speed of the water vapour is')
print var_x, '(m/s)^2'
#=============================The Standard Deviation============================#
#=====Now that we have calculated the variance we simpy take the square root====#
#=============================The Standard Deviation============================#
std_x = var_x**(.5)
print ('Finally the standard deviation in the speed of the water vapour is')
print std_x, '(m/s)'
