# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 19:08:25 2017

@author: Mr.Wang

In this programming problem and the next you'll code up the greedy algorithm 
from the lectures on Huffman coding.

Download the text file below.

huffman.txt
This file describes an instance of the problem. It has the following format:

[number_of_symbols]

[weight of symbol #1]

[weight of symbol #2]

...

For example, the third line of the file is "6852892," indicating that the
 weight of the second symbol of the alphabet is 6852892. (We're using weights 
 instead of frequencies, like in the "A More Complex Example" video.)

Your task in this problem is to run the Huffman coding algorithm from lecture 
on this data set. What is the maximum length of a codeword in the resulting 
Huffman code?

Continuing the previous problem, what is the minimum length of a codeword in your Huffman code?
"""

file="huffman.txt"
file=open(file,'r')
file=file.readlines()
data={}
record={}
for i in range(len(file)):
    data[int(file[i][:-1])]=[1,[i]]
    record[i]=1

while len(data)>2:
    min_cost1=min(data)
    set1=data.pop(min_cost1)
    min_cost2=min(data)
    set2=data.pop(min_cost2)
    new_length=max(set1[0],set2[0])+1      
    new_cost=min_cost1+min_cost2
    set1[1].extend(set2[1])
    data[new_cost]=[new_length,set1[1]]
    for i in set1[1]:
        record[i]+=1

print(min(record.values()))

