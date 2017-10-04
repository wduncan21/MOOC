# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 20:30:03 2017

@author: Mr.Wang
In this programming problem you'll code up the dynamic programming algorithm 
for computing a maximum-weight independent set of a path graph.

Download the text file below.

mwis.txt
This file describes the weights of the vertices in a path graph (with the 
weights listed in the order in which vertices appear in the path). It has the following format:

[number_of_vertices]

[weight of first vertex]

[weight of second vertex]

...

For example, the third line of the file is "6395702," indicating that the 
weight of the second vertex of the graph is 6395702.

Your task in this problem is to run the dynamic programming algorithm (and 
the reconstruction procedure) from lecture on this data set. The question is: 
of the vertices 1, 2, 3, 4, 17, 117, 517, and 997, which ones belong to the 
maximum-weight independent set? (By "vertex 1" we mean the first vertex of 
the graph---there is no vertex 0.) In the box below, enter a 8-bit string, 
where the ith bit should be 1 if the ith of these 8 vertices is in the 
maximum-weight independent set, and 0 otherwise. For example, if you think 
that the vertices 1, 4, 17, and 517 are in the maximum-weight independent set 
and the other four vertices are not, then you should enter the string 10011010
 in the box below.
"""
file=open('mwis.txt','r').readlines()
data=[]
for line in file:
    data.append(int(line[:-1]))

max1=data[0]
max_set1=[0]
max2=data[1]
max_set2=[1]
if max1>max2:
    max2=max1
    max_set2=max_set1
for i in range(2,len(data)):
    if max1+data[i]>max2:
        max1,max2=max2,max1+data[i]
        max_set1.append(i)
        max_set1,max_set2=max_set2.copy(),max_set1.copy()
    else:
        max1,max2=max2,max2
        max_set1,max_set2=max_set2.copy(),max_set2.copy()
if max1>max2:
    maxs,max_set=max1,max_set1
else:
    maxs,max_set=max2,max_set2
max_set=[i+1 for i in max_set]  
a=[1, 2, 3, 4, 17, 117, 517, 997]
print(''.join(['1' if i in max_set else '0' for i in a]))
