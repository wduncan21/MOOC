# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 21:54:24 2017

@author: Mr.Wang
"""

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L)==0:
        return float('NaN')
    else:
        total=0
        for i in L:
            total+=len(i)
        mean=total/len(L)
        sum_square=0
        for i in L:
            sum_square+=(len(i)-mean)**2
        return (sum_square/len(L))**(1/2.0)