# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 09:51:31 2019

@author: satya
"""

num=int(input("Enter any number"))
fact=[]

for i in range(num):
    while(num%(i+2)==0):
        num=num//(i+2)
        fact.append(i+2)
        
print(fact)