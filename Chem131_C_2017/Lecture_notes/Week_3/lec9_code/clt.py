# Lecture 9 Code, Central Limit Theorem
# This code will model rolling 4 dice, and plotting the frequency 
# of their average each trial (experiment = 4 dice rolled). 
# As we increase the number of experiments we approach
# a normal distribution. 

import numpy as np # numpy allows for more math functions
import matplotlib.pyplot as plt # matplotlib is for graphing

trials = 10000000 # trials for our experiment
n=0          # counting variable for the loop
x = []       # our averages for each experiment
while n< trials: # keep running experiments until we reach trials
    a = np.random.randint(1,6) 
    b = np.random.randint(1,6)
    c = np.random.randint(1,6)
    d = np.random.randint(1,6)
    y = (a+b+c+d) / 4.0
    x.append(y)
    n = n + 1

plt.hist(x)
plt.title('Central Limit Theorem 10000000 Trials')
plt.xlabel('Averge Value 4 Dice')
plt.ylabel('Frequency')
plt.savefig('clt10000000.png')
