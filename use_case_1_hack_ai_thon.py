# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 11:51:23 2019

@author: 1029693
"""
import matplotlib.pyplot as plt
import numpy as np
T=[]
Vel=[]
wind_chill=[]

for Temp in range(-20,70,10):
    for V in range(0,55,5):
        cal=35.74+(0.6215*Temp)-(35.75*(V**0.16))+(0.4275*Temp*(V**0.16))
        wind_chill.append(round(cal,2))
        T.append(Temp)
        Vel.append(V)
        print(Temp,V,cal)
    
len(wind_chill)
w_c=np.reshape(wind_chill,(9,11))


plt.plot(Vel,wind_chill)
plt.xlabel("Velocity")
plt.ylabel("Wind Chill")
plt.plot(T,wind_chill)
plt.xlabel("Temperature")
plt.ylabel("Wind Chill")
plt.plot(T,Vel)
plt.plot(wind_chill,Vel)
plt.plot(wind_chill,T)
plt.plot(Vel)
plt.plot(T) 

