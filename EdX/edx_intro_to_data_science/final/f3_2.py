# -*- coding: utf-8 -*-
"""
Created on Sun May  7 14:47:56 2017

@author: lwang138
"""

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    pos=0
    for i in range(numTrials):
        balls=[1,1,1,1,2,2,2,2]
        selected=[]
        for j in range(3):
            current=random.choice(balls)
            selected.append(current)
            balls.remove(current)
        if selected[0]==selected[1]==selected[2]:
            pos+=1
    return pos/float(numTrials)
        