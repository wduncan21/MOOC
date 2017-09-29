# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 10:59:07 2017

@author: lwang138
"""

import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    pools=[2*x for x in range(0,50)]
    return random.choice(pools)