# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 12:37:50 2017

@author: lwang138
"""

def word_distribution(text):
    words=text.lower().split()
    dic={}
    for word in words:
        if not word.isalpha():
            if not word[0].isalpha():
                word=word[1:]
            elif not word[-1].isalpha():
                word=word[:-1]
        if word in dic:
            dic[word]+=1
        else:
            dic[word]=1
    return dic