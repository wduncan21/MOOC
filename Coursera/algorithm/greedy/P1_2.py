# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 21:40:08 2017

@author: Mr.Wang
"""
"""
For this problem, use the same data set as in the previous problem.

Your task now is to run the greedy algorithm that schedules jobs (optimally) 
in decreasing order of the ratio (weight/length). In this algorithm, it does 
not matter how you break ties. You should report the sum of weighted completion
 times of the resulting schedule --- a positive integer --- in the box below.
"""
import numpy as np
import pandas as pd


file=pd.read_table("jobs.txt",sep=' ',header=None,names=['weight','length'])
file['ratio']=file['weight']/file['length']
file=file.sort_values(['ratio','weight'],ascending=False)
length = file['length'].values
cumulate_length = np.cumsum(length)
file['cumulate_length']=cumulate_length
file['weight*length']=file['cumulate_length']*file['weight']
print(file['weight*length'].sum())