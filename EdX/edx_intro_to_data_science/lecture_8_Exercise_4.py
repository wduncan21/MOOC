# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 22:04:29 2017

@author: Mr.Wang
"""

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    result=0
    for trials in range(numTrials):
        set=['r','r','r','g','g','g']
        for i in range(3):
            selected=random.choice(set)
            set.remove(selected)
        if set[0]==set[1]==set[2]:
            result+=1
    return result/numTrials
            