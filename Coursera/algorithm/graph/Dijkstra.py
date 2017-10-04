# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 23:42:10 2017

@author: Mr.Wang
"""

"""
In this programming problem you'll code up Dijkstra's shortest-path algorithm.

Download the following text file:

dijkstraData.txt
The file contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200. Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge. For example, the 6th row has 6 as the first entry indicating that this row corresponds to the vertex labeled 6. The next entry of this row "141,8200" indicates that there is an edge between vertex 6 and vertex 141 that has length 8200. The rest of the pairs of this row indicate the other vertices adjacent to vertex 6 and the lengths of the corresponding edges.

Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) as the source vertex, and to compute the shortest-path distances between 1 and every other vertex of the graph. If there is no path between a vertex v and vertex 1, we'll define the shortest-path distance between 1 and v to be 1000000.

You should report the shortest-path distances to the following ten vertices, in order: 7,37,59,82,99,115,133,165,188,197. You should encode the distances as a comma-separated string of integers. So if you find that all ten of these vertices except 115 are at distance 1000 away from vertex 1 and 115 is 2000 distance away, then your answer should be 1000,1000,1000,1000,1000,2000,1000,1000,1000,1000. Remember the order of reporting DOES MATTER, and the string should be in the same order in which the above ten vertices are given. The string should not contain any spaces. Please type your answer in the space provided.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Dijkstra's algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing the heap-based version. Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.
"""
f=open("B:\\OneDrive\\Documents\\coursera\\algorithm\\graph\\dijkstraData.txt","r")
test=f.readlines()
file=[x[:-1] for x in test]
f.close()
dic={}
## read file into the dictionary
for line in file:
    temp=line.split()
    val=temp[1:]
    temp_dict={}
    for i in val:
        temp_i=i.split(',')
        temp_dict[int(temp_i[0])]=int(temp_i[1])
    dic[int(temp[0])]=temp_dict

def cal_current_nei(current):
    ## calculate all the current neighbors' distance and remove current from unvisted list
    global unvisited,distance
    current_neib=dic[current]
    ## compute all next-to-current nodes distance
    for i in current_neib:
        if i not in distance:
            distance[i]=current_neib[i]+distance[current]
        else:
            distance[i]=min(distance[i],current_neib[i]+distance[current])
    unvisited.remove(current)
    
## set the initial values and start from 1
distance={1:0}
current=1
unvisited=[*dic]
next_set=[1]
## while there is something in the neighbors with calculated distance
while len(next_set)>0:
    # change current to the one with min distance
    current=sorted(next_set,key=lambda x:distance[x])[0]
    ## calculate its neighbors
    cal_current_nei(current)
    ## get the next set of calculatable neighbors
    next_set=set(unvisited).intersection(distance)
