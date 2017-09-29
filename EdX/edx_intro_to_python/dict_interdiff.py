# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 14:30:00 2017

@author: lwang138
"""

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    d1key=list(d1.keys())
    d2key=list(d2.keys())
    commonkey=list(set(d1key).intersection(d2key))
    uniqued1=set(d1key)-set(commonkey)
    uniqued2=set(d2key)-set(commonkey)
    common={}
    diff={}
    for i in commonkey:
        common[i]=f(d1[i],d2[i])
    for i in uniqued1:
        diff[i]=d1[i]    
    for i in uniqued2:
        diff[i]=d2[i]
    return(common,diff)