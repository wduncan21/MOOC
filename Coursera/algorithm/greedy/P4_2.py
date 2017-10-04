# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 21:54:04 2017

@author: Mr.Wang


This problem also asks you to solve a knapsack instance, but a much bigger one.

Download the text file below.

knapsack_big.txt
This file describes a knapsack instance, and it has the following format:

[knapsack_size][number_of_items]

[value_1] [weight_1]

[value_2] [weight_2]

...

For example, the third line of the file is "50074 834558", indicating that the 
second item has value 50074 and size 834558, respectively. As before, you should
 assume that item weights and the knapsack capacity are integers.

This instance is so big that the straightforward iterative implemetation uses 
an infeasible amount of time and space. So you will have to be creative to 
compute an optimal solution. One idea is to go back to a recursive implementation, solving subproblems --- and, of course, caching the results to avoid redundant work --- only on an "as needed" basis. Also, be sure to think about appropriate data structures for storing and looking up solutions to subproblems.

In the box below, type in the value of the optimal solution.

ADVICE: If you're not getting the correct answer, try debugging your algorithm 
using some small test cases. And then post them to the discussion forum!
"""
import sys
sys.setrecursionlimit(2 ** 20)
file='B:\\OneDrive\\Documents\\coursera\\algorithm\\greedy\\knapsack_big.txt'
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
C={}
def knapsack(size,n):
    key=str(size) + ',' + str(n)
    if n==0:
        return 0
    if key in C:
        return C[key]
    else:
        if weights[n-1]>size:
            C[key]=knapsack(size,n-1)
        else:
            C[key]=max(knapsack(size,n-1),knapsack(size-weights[n-1],n-1)+values[n-1])
        return C[key]

res=knapsack(max_weight,n)
print(res)

