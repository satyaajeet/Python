# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 15:28:49 2019

@author: satya
"""
int1_factors=[]
int2_factors=[]
print("Enter two numbers")
int1=int(input())
int2=int(input())
for i in range(int1//2):
    if int1%(i+1)==0:
        int1_factors.append(i+1)
    else:
        continue

for i in range(int2//2):
    if int2%(i+1)==0:
        int2_factors.append(i+1)
    else:
        continue

print(int1_factors)
print(int2_factors)

multiple=int1*int2
mult_factors=[]
print(multiple)
for i in range(multiple//2):
    if multiple%(i+1)==0:
        mult_factors.append(i+1)
    else:
        continue
print(mult_factors)
final=int1_factors+int2_factors
print(final)

final=list(dict.fromkeys(final))
final.sort()
print(final)

LCM=1
for i in range(len(final)):
    LCM=LCM*final[i]
    
print(LCM)


            


