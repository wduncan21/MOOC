# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 23:14:24 2017

@author: Mr.Wang
"""

def main():
    global dic,order,dic_rev,visited,scc
    f=open("B:\\OneDrive\\Documents\\coursera\\algorithm\\graph\\SCC.txt","r")
    test=f.readlines()
    file=[x[:-1] for x in test]

    dic={}
    dic_rev={}
## read file into the dictionary and reverse ones
    for line in file:
        temp=line.split()
        if int(temp[0]) not in dic.keys():
            dic[int(temp[0])]=[int(temp[1])]
        else:
            dic[int(temp[0])].append(int(temp[1]))
           
        if int(temp[1]) not in dic_rev.keys():
            dic_rev[int(temp[1])]=[int(temp[0])]
        else:
            dic_rev[int(temp[1])].append(int(temp[0]))
            f.close()
            ## catch all the nodes
    a=list(dic.keys())
    b=list(dic_rev.keys())
    a.extend(b)
    nodes=list(set(a))
    nodes.sort()

    visited={}
    order=[]
    for i in nodes:
        if i not in visited:
            visit_1(i,visited)

    visited={}
    res=[]
    while order:
        i=order.pop()
        if i not in visited:
            scc=[]
            visit_2(i,visited)
            res.append(len(scc))
    if len(res)<5:
        print(sorted(res,reverse=True))
    else:
        print(sorted(res,reverse=True)[:5])
##Let's do the reverse round first
def visit_1(i,visited):
    visited[i]=True
    if i in dic:
        for j in dic[i]:
            if j not in visited:
                visit_1(j,visited)
    order.append(i)
## Let's do second round

def visit_2(i,visited):
    visited[i]=True
    scc.append(i)
    if i in dic_rev:
        for j in dic_rev[i]:
            if j not in visited:
                visit_2(j,visited)
                
import threading,sys
threading.stack_size(67108864) # 64MB stack
sys.setrecursionlimit(2 ** 20) # approx 1 million recursions
thread = threading.Thread(target = main) # instantiate thread object
thread.start() # run program at target
