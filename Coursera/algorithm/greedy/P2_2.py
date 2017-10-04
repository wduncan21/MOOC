# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 22:15:15 2017

@author: Mr.Wang
"""
"""
In this question your task is again to run the clustering algorithm from 
lecture, but on a MUCH bigger graph. So big, in fact, that the distances (i.e., edge costs) are only defined implicitly, rather than being provided as an explicit list.

The data set is below.

clustering_big.txt
The format is:

[# of nodes] [# of bits for each node's label]

[first bit of node 1] ... [last bit of node 1]

[first bit of node 2] ... [last bit of node 2]

...

For example, the third line of the file "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 
1 0 1 1 0 1" denotes the 24 bits associated with node #2.

The distance between two nodes u and v in this problem is defined as the 
Hamming distance--- the number of differing bits --- between the two nodes' 
labels. For example, the Hamming distance between the 24-bit label of node 
#2 above and the label "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1" is 3
 (since they differ in the 3rd, 7th, and 21st bits).

The question is: what is the largest value of k such that there is a 
k-clustering with spacing at least 3? That is, how many clusters are needed 
to ensure that no pair of nodes with all but 2 bits in common get split into 
different clusters?

NOTE: The graph implicitly defined by the data file is so big that you probably
 can't write it out explicitly, let alone sort the edges by cost. So you will 
 have to be a little creative to complete this part of the question. For 
 example, is there some way you can identify the smallest distances without 
 explicitly looking at every pair of nodes?
"""
import pandas as pd
#file=pd.read_table("B:\\OneDrive\\Documents\\coursera\\algorithm\\greedy\\input_random_10_16_18.txt",sep=' ',header=None,names=list(range(1,26)))
#file=file.drop(25,1)
file=pd.read_table("B:\\OneDrive\\Documents\\coursera\\algorithm\\greedy\\input\
_random_10_16_18.txt",sep=' ',header=None,names=list(range(1,16)))
#file=file.drop(25,1)
file = file.astype(int)
dic={}
for i in range(len(file)):
    string=''.join(map(str, list(file.iloc[i])))
    dic[string]=1

def find_friends(line):
    friends=[]
    for i in range(len(line)):
        temp_line=line.copy()
        temp_line[i]=abs(temp_line[i]-1)
        friends.append(temp_line)
    for i in range(len(line)):
        for j in range(len(line)):
            if i!=j:
                temp_line=line.copy()
                temp_line[i]=abs(temp_line[i]-1)
                temp_line[j]=abs(temp_line[j]-1)
                friends.append(temp_line)
    return friends
checked={}
num=0
for j in range(len(file)):
    i=list(file.iloc[j])
    str_i=''.join(map(str, i))
    if str_i in checked:
        continue
    checked[str_i]=1
    same_cluster=[]
    same_cluster.extend(find_friends(i))
    while len(same_cluster)>0:
        fri=same_cluster[0]
        str_fri=''.join(map(str, fri))
        if str_fri not in checked:
            if str_fri in dic:
                checked[str_fri]=1
                same_cluster.extend(find_friends(fri))
        same_cluster.pop(0)
    num+=1
print(num)