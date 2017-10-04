# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 17:08:25 2017

@author: Mr.Wang
"""
## read in file into list and remove the \n
f = open('B:/OneDrive/Documents/coursera/algorithm/divide/IntegerArray.txt', 'r')
test=f.readlines()
file=[x[:-1] for x in test]
file=[int(x) for x in file]
f.close()

test=[1,2,5,4,3]

## define function to count inversions

def inversion(input):
    length=len(input)
    if length==1:
        return 0,input
    else:
        cut=int(length/2)
        left=input[0:cut]
        right=input[cut:]
        ## get the inversion on the left and on the right
        x_count,x_sort=inversion(left)
        y_count,y_sort=inversion(right)
        ## get the count for comparing left and right
        ## sort the array
        count=0
        sort=[]            
        i=j=0
        while i<len(x_sort) and j<len(y_sort):
            if x_sort[i]<=y_sort[j]:
                sort.append(x_sort[i])
                i+=1
            else:
                sort.append(y_sort[j])
                count=count+len(x_sort)-i ## this means for the current y, all the x's remaining are inversions    
                j+=1
        ## append any left x and y's
        sort.extend(x_sort[i:])
        sort.extend(y_sort[j:])
        current_count=x_count+y_count+count
        return current_count,sort
        
    