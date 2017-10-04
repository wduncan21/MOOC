# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:04:15 2017

@author: Mr.Wang
"""
"""
In this programming problem and the next you'll code up the clustering
 algorithm from lecture for computing a max-spacing k-clustering.

Download the text file below.

clustering1.txt
This file describes a distance function (equivalently, a complete graph with
 edge costs). It has the following format:

[number_of_nodes]

[edge 1 node 1] [edge 1 node 2] [edge 1 cost]

[edge 2 node 1] [edge 2 node 2] [edge 2 cost]

...

There is one edge (i,j) for each choice of 1≤i<j≤n, where n is the number of nodes.

For example, the third line of the file is "1 3 5250", indicating that the
 distance between nodes 1 and 3 (equivalently, the cost of the edge (1,3)) 
 is 5250. You can assume that distances are positive, but you should NOT 
 assume that they are distinct.

Your task in this problem is to run the clustering algorithm from lecture on 
this data set, where the target number k of clusters is set to 4. What is the 
maximum spacing of a 4-clustering?

"""
import pandas as pd
import numpy as np

file=pd.read_table("B:\\OneDrive\\Documents\\coursera\\algorithm\\greedy\\clustering1.txt",sep=' ',header=None,names=['N1','N2','cost'])
file=file.sort_values(['cost'],ascending=True)
nodes=list(set(np.append(file['N1'].values,file['N2'].values)))
dic={}
clusters={}
for i in nodes:
    dic[i]=i
    clusters[i]=[i]
number=len(set(dic.values()))
i=0
while number!=4:
    a=file.iloc[i][0]
    b=file.iloc[i][1]
    lead_a=dic[a]
    lead_b=dic[b]
    if lead_a!=lead_b:
        size_a=len(clusters[lead_a])
        size_b=len(clusters[lead_b])
        if size_a>size_b:
            clusters[lead_a]+=clusters[lead_b]
            for i in clusters[lead_b]:
                dic[i]=lead_a
            clusters.pop(lead_b)
        else:
            clusters[lead_b]+=clusters[lead_a]
            for i in clusters[lead_a]:
                dic[i]=lead_b
            clusters.pop(lead_a)
    number=len(clusters)
    i+=1
res={}
for j in range(i,len(file)):
    a=file.iloc[j][0]
    b=file.iloc[j][1]
    lead_a=dic[a]
    lead_b=dic[b]
    
    if lead_a!=lead_b:
        pair=str(sorted([lead_a,lead_b]))
        if pair not in res:
            res[pair]=file.iloc[j][2]
min(res.values())