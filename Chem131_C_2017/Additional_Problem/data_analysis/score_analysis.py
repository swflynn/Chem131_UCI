# Quick Data Analysis for Midterm Scores
# The code reads in a file with 2 colums: ID# Score
# The code reads in data line by line to a list, it then splits the list into 2 columns
# then we convert the list to decimals and do basic statistical analysis
# Please note there are better ways to do this (statistics package in python)
# This is simply an example using very little programming to get useful results!

import numpy as np
import matplotlib.pyplot as plt

# Read in data from scores.dat data file
with open('scores.dat') as f:                       #open the data file
    lines = f.readlines()                           #read in data line-by-line
    x = [line.split()[0] for line in lines]         #x = student id
    z = [line.split()[1] for line in lines]         #z = midterm score (I removed score=0)

# Convert list y into float so we can do math on it (list gives strings not decimals). 
y = []
for item in z:
    y.append(float(item))

# Determine how many exams there are
number_exams = len(y)
print('%r people took the exam')% number_exams

# determine the lowest score
low_s = min(float(a) for a in y)
print('The lowest score on the exam was %r')% low_s

# determine the highest score
high_s = max(float(b) for b in y)
print('The highest score on the exam was %r')% high_s

#the unweighted average
ave = sum(y)/ number_exams
print('The unweighted average for the exam was %r')% ave

# the median exam score
mead = np.median(y)
print('The median exam score was %r')% mead

# the standard deviation for the exam scores (population)
stdev = np.std(y)
print('The standard deviation for the entire population is %r')% stdev

# Frequency Histogram for the exam scores. 
plt.hist(y, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
plt.title('Exam Score Histogram')
plt.show()
