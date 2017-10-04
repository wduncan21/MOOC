# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 22:00:00 2017

@author: Mr.Wang
"""
f=open("B:/OneDrive/Documents/coursera/algorithm/divide/kargerMinCut.txt")
file=f.readlines()
dic={}
import random
for line in file:
    temp_list=line.split()
    dic[int(temp_list[0])]=[int(x) for x in temp_list[1:]]

import copy
result=[]
seed=0
## sample 1000 times
for i in range(1000):
    dict_loop=copy.deepcopy(dic)
    seed+=1
    random.seed(seed)
    ## while graph not reduced to 2 vertices, repeat
    while len(dict_loop)>2:
        ## sample the two merged vertices
        a=random.sample(list(dict_loop.keys()),1)[0]
        b=random.sample(dict_loop[a],1)[0]
        ## b will be merged with a
        merged=dict_loop[b]
        ## if b linked with a, remove a
        while a in merged:
            merged.remove(a)
            dict_loop[a].remove(b)
        ## from the dict, remove b, since b will be merged with a
        dict_loop.pop(b)
        ## extend the a edges by adding all the b ones
        dict_loop[a].extend(merged)
        ## if b connects with a, remove b
        #while b in dict_loop[a]:dict_loop[a].remove(b)
        
        ## for all the ones connect with b, add a there, 
        #for key in list(set(merged)):
            #count=dict_loop[key].count(b)
            #while b in dict_loop[key]: dict_loop[key].remove(b)
            #dict_loop[key].extend([a]*count)
        for key in merged:
            dict_loop[key].remove(b)
            dict_loop[key].extend([a])
        
    result.append(len(list(dict_loop.values())[0]))
print(min(result))