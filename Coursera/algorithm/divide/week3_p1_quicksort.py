# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 22:18:35 2017

@author: Mr.Wang
"""
f = open('B:/OneDrive/Documents/coursera/algorithm/divide/QuickSort.txt', 'r')
test=f.readlines()
file=[x[:-1] for x in test]
file=[int(x) for x in file]
f.close()


data_tuples = list()
with open('sample_data.csv','r') as f:
    for line in f:
        data_tuples.append(line.strip().split(','))
        
## question 1
## count the number of comparisons by using first element as pivot
## read in file into list and remove the \n

def quicksort(list):

    if len(list)<2:
        return list,0
    pivot=list[0]
    i=1
    count=len(list)-1
    for id in range(1,len(list)):
        if list[id]<pivot:
            temp=list[i]
            list[i]=list[id]
            list[id]=temp
            i+=1
    left,l_count=quicksort(list[1:i])
    
    right,r_count=quicksort(list[i:])
    
    return left+[list[0]]+right,count+l_count+r_count


## question 2
## count the number of comparisons by using last element as pivot

def quicksort_last(list):

    if len(list)<2:
        return list,0
    pivot=list[-1]
    i=0
    count=len(list)-1
    for id in range(0,len(list)-1):
        if list[id]<pivot:
            temp=list[i]
            list[i]=list[id]
            list[id]=temp
            i+=1
    left,l_count=quicksort(list[0:i])
    
    right,r_count=quicksort(list[i:-1])
    
    return left+[list[-1]]+right,count+l_count+r_count


## question 2
## count the number of comparisons by using last element as pivot

def quicksort_three(list):

    if len(list)<2:
        return list,0
    from statistics import median
    pivot1=list[0]
    pivot2=list[int(len(list)/2)]
    pivot3=list[-1]
    pivot=median([pivot1,pivot2,pivot3])
    list.remove(pivot)
    i=0
    count=len(list)
    for id in range(0,len(list)):
        if list[id]<pivot:
            temp=list[i]
            list[i]=list[id]
            list[id]=temp
            i+=1
    left,l_count=quicksort(list[:i])
    
    right,r_count=quicksort(list[i:])
    
    return left+[pivot]+right,count+l_count+r_count