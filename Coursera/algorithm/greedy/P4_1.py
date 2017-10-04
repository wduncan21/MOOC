# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 21:13:03 2017

@author: Mr.Wang

In this programming problem and the next you'll code up the knapsack algorithm 
from lecture.

Let's start with a warm-up. Download the text file below.

knapsack1.txt
This file describes a knapsack instance, and it has the following format:

[knapsack_size][number_of_items]

[value_1] [weight_1]

[value_2] [weight_2]

...

For example, the third line of the file is "50074 659", indicating that the 
second item has value 50074 and size 659, respectively.

You can assume that all numbers are positive. You should assume that item 
weights and the knapsack capacity are integers.

In the box below, type in the value of the optimal solution.

ADVICE: If you're not getting the correct answer, try debugging your algorithm
 using some small test cases. And then post them to the discussion forum!
"""
file='knapsack1.txt'
data=open(file,'r')
lines=data.readlines()
values=[]
weights=[]
max_weight=int(lines[0].split()[0])
for line in lines[1:]:
    value,weight=line.split()
    values.append(int(value))
    weights.append(int(weight))
    
n=len(values)
temp={}
def knapsack(values,weights,max_weight,n):
    for i in range(n+1):
        for j in range(max_weight+1):        
            if i==0:
                temp[(i,j)]=0
            else:
                if weights[i-1]>j:
                    temp[(i,j)]=temp[(i-1,j)]
                else:
                    temp[(i,j)]=max(temp[(i-1,j)],temp[(i-1,j-weights[i-1])]+values[i-1])
    return temp[(n,max_weight)]

res=knapsack(values,weights,max_weight,n)
print(res)