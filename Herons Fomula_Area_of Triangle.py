# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:34:44 2019

@author: 1029693
"""

#Area of triangle using Heron's Formula
import math
def getTriangleArea(x, y):
    # Write your code here
    p=math.sqrt((((x[0]-x[1])**2)+((y[0]-y[1])**2)))
    q=math.sqrt((((x[1]-x[2])**2)+((y[1]-y[2])**2)))
    r=math.sqrt((((x[0]-x[2])**2)+((y[0]-y[2])**2)))

    s=(p+q+r)/2

    area=math.sqrt(s*(s-p)*(s-q)*(s-r))
    
    return math.ceil(area)

x=(0,3,6)
y=(0,3,0)
res=getTriangleArea(x, y)

print(res)

