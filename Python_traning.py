# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 19:13:49 2019

@author: satya
"""

import random

square={a:a*a for a in range(10)}
print(square)

a=[]
for j in range(10):
    for i in range(10):
        a.append(random.randint(1,10))

print(a)
print(sum)