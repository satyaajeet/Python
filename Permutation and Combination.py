#!/usr/bin/env python
# coding: utf-8

# In[88]:


import math


# In[98]:


#Find permutations for a string s and using k element at a time.
def nposperm(s,k) : # s string k is size
    c1=len(s)
    tot=0
    while k>0:
        tot+=(math.factorial(c1)/(math.factorial(c1-k)))
        k=k-1
    return int(tot)
 
nposperm("HACK",4)


# In[90]:


#Combinations
def nposcomb(s,k):
    c1=len(s)
    tot=0
    while k>0:
        tot+=math.factorial(c1)/(math.factorial(k)*math.factorial(c1-k))
        k=k-1
    return int(tot)
nposcomb("HACK",2)


# In[91]:


#How many combinations are possible if we can replace the characters of the string s by chosing k characters at random
def nposcombrep(s,k):
    c1=len(s)
    tot=0
    tot=math.factorial(c1+k-1)/(math.factorial(k)*math.factorial(c1-1))
    return int(tot)

nposcombrep("HACK",3)


# In[96]:


#With replacement possible, how many permutations are possible for a stringg s and k characters chosen at random
def npospermrep(s,k):
    c1=len(s)
    tot=0
    tot=c1**k
    return tot
npospermrep("HACK",4)


# In[93]:


#Out of 56 card of a deck, you have to chose 30 cards. of those 30 cards, You have to chose 'r' red cards out of 26 reds and 
#'b' black cards out of 26 black cards. Find the number of combination of the cards possible if 22 red and 8 black cards are chosen
def cards(r,b):
    tot=0
    tot=(math.factorial(26)/(math.factorial(r)*math.factorial(26-r)))*(math.factorial(26)/(math.factorial(b)*math.factorial(26-b)))
    return int(tot)
cards(22,8)

