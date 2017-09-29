# -*- coding: utf-8 -*-
"""
Created on Sun May  7 15:29:52 2017

@author: lwang138
"""

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    import itertools
    import numpy as np
    bins = np.array(list(itertools.product([0, 1], repeat=len(choices))))
    combo=[bin for bin in bins if sum(bin*choices)==total]
    if combo:
        return (min(combo,key=sum))
    else:
        return max([bin for bin in bins if sum(bin*choices)<total],key=sum)