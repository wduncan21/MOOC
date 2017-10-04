# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 21:48:49 2017

@author: Mr.Wang
"""
"""
This file describes an undirected graph with integer edge costs. It has the 
format

[number_of_nodes] [number_of_edges]

[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]

[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]

...

For example, the third line of the file is "2 3 -8874", indicating that there 
is an edge connecting vertex #2 and vertex #3 that has cost -8874.

You should NOT assume that edge costs are positive, nor should you assume that 
they are distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph. You 
should report the overall cost of a minimum spanning tree --- an integer, which 
may or may not be negative --- in the box below.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) 
time implementation of Prim's algorithm should work fine. OPTIONAL: For those 
of you seeking an additional challenge, try implementing a heap-based version.
 The simpler approach, which should already give you a healthy speed-up, is to 
 maintain relevant edges in a heap (with keys = edge costs). The superior 
 approach stores the unprocessed vertices in the heap, as described in lecture. 
 Note this requires a heap that supports deletions, and you'll probably need 
 to maintain some kind of mapping between vertices and their positions in the 
 heap.
"""
import numpy as np
import pandas as pd


file=pd.read_table("edges.txt",sep=' ',header=None,names=['v1','v2','cost'])
vertex=list(set(np.append(file['v1'].values,file['v2'].values)))
v1=np.append(file['v1'].values,file['v2'].values)
v2=np.append(file['v2'].values,file['v1'].values)
costs=np.append(file['cost'].values,file['cost'].values)
uni_file=pd.DataFrame({'v1':v1,'v2':v2,'costs':costs})
explored=[1]
unexplored=vertex.copy()
unexplored.remove(1)
boundry=uni_file[uni_file['v1']==1]
cost=0
loop=0
while len(unexplored):#while len(unexplored)>1:
    loop+=1
    new=boundry[boundry['costs']==boundry['costs'].min()]['v2'].values
    cost+=boundry['costs'].min()
    explored.append(new[0])
    unexplored.remove(new[0])
    new_edges=uni_file[uni_file['v1']==new[0]]
    boundry=pd.concat([boundry,new_edges])
    boundry=boundry[[x not in explored for x in boundry['v2'].values]]

print(cost)