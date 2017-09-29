# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 14:25:58 2017

@author: lwang138
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    L.reverse()
    for i in range(len(L)):
        L[i].reverse()
    