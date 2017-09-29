# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 16:30:30 2017

@author: Mr.Wang
"""

def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def evaluate(x):
        length=len(L)-1
        value=0
        for i in L:
            value+=i*(x**length)
            length-=1
        return value
    return evaluate