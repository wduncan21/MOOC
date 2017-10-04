# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 21:18:05 2017

@author: Mr.Wang
"""
"""
This file describes a set of jobs with positive and integral weights and 
lengths. It has the format

[number_of_jobs]

[job_1_weight] [job_1_length]

[job_2_weight] [job_2_length]

...

For example, the third line of the file is "74 59", indicating that the second 
job has weight 74 and length 59.

You should NOT assume that edge weights or lengths are distinct.

Your task in this problem is to run the greedy algorithm that schedules jobs 
in decreasing order of the difference (weight - length). Recall from lecture 
that this algorithm is not always optimal. IMPORTANT: if two jobs have equal 
difference (weight - length), you should schedule the job with higher weight 
first. Beware: if you break ties in a different way, you are likely to get the 
wrong answer. You should report the sum of weighted completion times of the 
resulting schedule --- a positive integer --- in the box below.
"""
import numpy as np
import pandas as pd

file=pd.read_table("jobs.txt",sep=' ',header=None,names=['weight','length'])
file['diff']=file['weight']-file['length']
file=file.sort_values(['diff','weight'],ascending=False)
length = file['length'].values
cumulate_length = np.cumsum(length)
file['cumulate_length']=cumulate_length
file['weight*length']=file['cumulate_length']*file['weight']
print(file['weight*length'].sum())