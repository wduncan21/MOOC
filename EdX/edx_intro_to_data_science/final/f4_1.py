# -*- coding: utf-8 -*-
"""
Created on Sun May  7 14:55:58 2017

@author: lwang138
"""
## support function
import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, bins=numBins)
    #pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title!=None:
        pylab.title(title)
    pylab.show()
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    Long_run_result=[]
    for trials in range(numTrials):
        long_run=0
        current_run=0
        last_num=0
        for rolls in range(numRolls):
            current_num=die.roll()
            if current_num==last_num:
                current_run+=1
            else:
                current_run=1
            if current_run>long_run:
                long_run=current_run
            last_num=current_num
        Long_run_result.append(long_run)
    makeHistogram(Long_run_result, 10, 'longest_runs', 'number of times')
    return getMeanAndStd(Long_run_result)[0]
            
    
# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))
