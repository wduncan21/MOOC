# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 14:44:32 2017

@author: lwang138
"""

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    Lcopy=L[:]
    
    for i in Lcopy:
        if not g(f(i)):
            L.remove(i)
    if len(L)==0:
        return -1
    else:
        return max(L)