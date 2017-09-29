# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 12:30:28 2017

@author: lwang138
"""

def max_contig_sum(A):
    """ A, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
    
    