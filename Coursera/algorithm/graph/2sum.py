# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 19:45:47 2017

@author: Mr.Wang
"""
"""
The goal of this problem is to implement a variant of the 2-SUM algorithm .

The file contains 1 million integers, both positive and negative (there might 
be some repetitions!).This is your array of integers, with the ith row of the 
file specifying the ith entry of the array.

Your task is to compute the number of target values t in the interval [-10000,
10000] (inclusive) such that there are distinct numbers x,yin the input file 
that satisfy x+y=t. (NOTE: ensuring distinctness requires a one-line addition 
to the algorithm from lecture.)

Write your numeric answer (an integer between 0 and 20001) in the space provided.
"""
"""
Overall idea: slice numbers into 5million bins, where i in bin=int(i/20000)
for each i, we only need to check the bin where -10000-i and 10000-i is in.
Effectively the algrithm is O(n)
"""
f=open("algo1-programming_prob-2sum.txt",'r')
lines=f.readlines()
lines=[int(x) for x in lines]
f.close()

## record how many times each number occurs, some might occur twice
input_count={}
for i in lines:
    if i in input_count:
        input_count[i]+=1
    else:
        input_count[i]=1
## assign each number into the bins
input_dict={}
for i in lines:
    if int(i/20000) in input_dict:
        input_dict[int(i/20000)].append(i)
    else:
        input_dict[int(i/20000)]=[i]

res={}
for i in lines:
    ## will only need to check bin lower and higher
    lower=int((-10000-i)/20000)
    higher=int((10000-i)/20000)
    if lower in input_dict:
        for j in input_dict[lower]:
            if i+j in range(-10000,10001):
                ## need to confirm if i==j, i appeared twice in list
                if i==j and input_count[i]==1:
                    continue
                res[i+j]=1
    if higher in input_dict:
        for j in input_dict[higher]:
            if i+j in range(-10000,10001):
                if i==j and input_count[i]==1:
                    continue
                res[i+j]=1
print (len(res))