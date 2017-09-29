# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 14:23:11 2017

@author: lwang138
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    sum=0
    for i in range(len(listA)):
        sum+=listA[i]*listB[i]
        
    return sum