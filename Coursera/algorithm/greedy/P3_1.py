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
"""

file="huffman.txt"
input=open(file,'r')
input=input.readlines()
data={}
for i in range(len(input)):
    data[int(input[i][:-1])]=1

    
while len(data)>2:
    key1=min(data)
    min1=data.pop(key1)
    key2=min(data)
    min2=data.pop(key2)
    min0=max(min1,min2)+1
    key=key1+key2
    data[key]=min0

print(max(data.values()))

