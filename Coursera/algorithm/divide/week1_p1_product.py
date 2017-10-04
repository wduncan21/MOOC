# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 23:13:07 2017

@author: Mr.Wang
"""

x=3141592653589793238462643383279502884197169399375105820974944592

y=2718281828459045235360287471352662497757247093699959574966967627

def karatsuba(x,y):
    ## change x, y into strings
    x_str=str(x)
    y_str=str(y)
    base_len=min(len(x_str),len(y_str))
    
    ##if x and y are both single digits, return x*y
    if base_len<2:
        return x*y
    else:
        cutoff=int(base_len/2)
        ## cut x and y into 4 parts
        ## key: divide from the right using negative index
        x_up=int(x_str[:-cutoff])
        x_down=int(x_str[-cutoff:])
        y_up=int(y_str[:-cutoff])
        y_down=int(y_str[-cutoff:])
        up_up= karatsuba(x_up,y_up)
        down_down=karatsuba(x_down,y_down)
        up_down=karatsuba((x_up+x_down),(y_up+y_down))-up_up-down_down
        return int(up_up*10**(cutoff*2)  +up_down*10**cutoff  +down_down)

print(karatsuba(x,y))
print(x*y)