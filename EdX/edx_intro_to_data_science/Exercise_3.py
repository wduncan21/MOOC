# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 11:04:43 2017

@author: lwang138
"""

import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return 10
    
    
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    pools=[2*x for x in range(5,11)]
    return random.choice(pools)
    