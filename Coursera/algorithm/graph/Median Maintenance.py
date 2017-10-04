# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 21:50:32 2017

@author: Mr.Wang
"""
"""
The goal of this problem is to implement the "Median Maintenance" algorithm 
(covered in the Week 3 lecture on heap applications). The text file contains 
a list of the integers from 1 to 10000 in unsorted order; you should treat 
this as a stream of numbers, arriving one by one. Letting xi denote the ith 
number of the file, the kth median mk is defined as the median of the numbers 
x1,…,xk. (So, if k is odd, then mk is ((k+1)/2)th smallest number among x1,…,
xk; if k is even, then mk is the (k/2)th smallest number among x1,…,xk.)

In the box below you should type the sum of these 10000 medians, modulo 10000 
(i.e., only the last 4 digits). That is, you should compute (m1+m2+m3+⋯+m10000)
mod10000.

OPTIONAL EXERCISE: Compare the performance achieved by heap-based and search-
tree-based implementations of the algorithm.
"""
import heapq


f=open("B:\\OneDrive\\Documents\\coursera\\algorithm\\graph\\median.txt","r")
test=f.readlines()
file=[int(x[:-1]) for x in test]
f.close()

H_low=[]
H_high=[]
sum_med=0
for x in file:
    if len(H_low)==0:
        heapq.heappush(H_low,-x)
    else:
        if x >-H_low[0]:
            heapq.heappush(H_high,x)
        else:
            heapq.heappush(H_low, -x)
    if len(H_low)<len(H_high):
         heapq.heappush(H_low,-heapq.heappop(H_high))
    elif len(H_low)>len(H_high)+1:
        heapq.heappush(H_high,-heapq.heappop(H_low))
    sum_med+=-H_low[0]
print(sum_med%10000)