# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 15:13:36 2017

@author: Mr.Wang
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    #two lists to store the current longest one and the new one
    bestup_now=[L[0]]
    bestup_new=[L[0]]

    bestdown_now=[L[0]]
    bestdown_new=[L[0]]
    for i in L[1:]:
        ## test increase first, if not decrease, add to the new bestup
        if i >=bestup_new[-1]:
            bestup_new.append(i)
        else: ## if decrease, test if bestup_new is longer than current best up,
            if len(bestup_new)>len(bestup_now): # if yes, change bestup_now=bestup_new
                bestup_now=bestup_new
            # change bestup_new=i to start no matter the above if
            bestup_new=[i]
        ## after finish looping, test if the last set is better
        if len(bestup_new)>len(bestup_now):
            bestup_now=bestup_new
            
        if i <=bestdown_new[-1]:
            bestdown_new.append(i)
        else: ## if decrease, test if bestup_new is longer than current best up,
            if len(bestdown_new)>len(bestdown_now): # if yes, change bestup_now=bestup_new
                bestdown_now=bestdown_new
            # change bestup_new=i to start no matter the above if
            bestdown_new=[i]
         ## after finish looping, test if the last set is better
        if len(bestdown_new)>len(bestdown_now):
            bestdown_now=bestdown_new
            
    if len(bestup_now)>len(bestdown_now):
        return sum(bestup_now)
    elif len(bestup_now)<len(bestdown_now):
        return sum(bestdown_now)
    elif [i for i in range(len(L)) if bestup_now==L[i:i+len(bestup_now)]][0]<[i for i in range(len(L)) if bestdown_now==L[i:i+len(bestup_now)]][0]:
        return sum(bestup_now)
    else:
        return sum(bestdown_now)