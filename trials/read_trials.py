#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 09:41:19 2022

@author: tercio
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math


df=pd.read_csv('trial_1.csv', sep=',',header=0)
df = np.array(df)

time = df[:,0]
time = time-time[0] #set time


mouse = np.zeros(len(time))

for i in range(len(df[:,1])):
    mouse[i] = math.sqrt((df[i,1]**2) + (df[i,2]**2))
    



target = math.sqrt((df[0,3]**2) + (df[0,4]**2))


plt.plot(time, mouse)
plt.plot(time[-1], target, 'ro')






