# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 22:47:47 2017

@author: Mr.Wang
In this assignment we will revisit an old friend, the traveling salesman
 problem (TSP). This week you will implement a heuristic for the TSP, rather
 than an exact algorithm, and as a result will be able to handle much larger 
 problem sizes. Here is a data file describing a TSP instance (original 
 source: http://www.math.uwaterloo.ca/tsp/world/bm33708.tsp).

nn.txt
The first line indicates the number of cities. Each city is a point in the 
plane, and each subsequent line indicates the x- and y-coordinates of a 
single city.

The distance between two cities is defined as the Euclidean distance --- 
that is, two cities at locations (x,y) and (z,w) have distance 
(x−z)2+(y−w)2−−−−−−−−−−−−−−−√ between them.

You should implement the nearest neighbor heuristic:

Start the tour at the first city.
Repeatedly visit the closest city that the tour hasn't visited yet. In case 
of a tie, go to the closest city with the lowest index. For example, if both
 the third and fifth cities have the same distance from the first city (and 
 are closer than any other city), then the tour should begin by going from the
 first city to the third city.
Once every city has been visited exactly once, return to the first city to 
complete the tour.
In the box below, enter the cost of the traveling salesman tour computed by 
the nearest neighbor heuristic for this instance, rounded down to the nearest 
integer.

[Hint: when constructing the tour, you might find it simpler to work with 
squared Euclidean distances (i.e., the formula above but without the square
 root) than Euclidean distances. But don't forget to report the length of the
 tour in terms of standard Euclidean distance.]
"""
file=open("nn.txt")
file=file.readlines()
cities={}
ids=[]
for i in file:
    city,x,y=i[:-1].split(' ')
    cities[int(city)]=[float(x),float(y)]
    ids.append(int(city))
city_1=cities[1]

cost=0
current=1
import math
while len(ids)>1:
    current_x,current_y=cities[current]
    ids.remove(current)
    
    min_loc=math.inf
    min_city=1
    round=list(cities.keys()).sort()
    for i in ids:
        x,y=cities[i]
        dif=(x-current_x)**2+(y-current_y)**2
        if dif<min_loc:
            min_loc=dif
            min_city=i
    cost+=min_loc**0.5
    current=min_city

cost+=((city_1[0]-cities[current][0])**2+(city_1[1]-cities[current][1])**2)**0.5
        
cost