# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 13:48:07 2017

@author: lwang138
"""

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    sum_mul=0
    for i in L:
        if s>=i:
            sum_mul+=s//i
            s=s%i
    if s==0:
        return sum_mul
    else:
        return "no solution"