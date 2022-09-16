# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 08:20:56 2022

@author: 90537
"""

import matplotlib.pyplot as plt
import numpy as np
theta=np.linspace(0,12*np.pi,10000)
x=np.sin(theta)*(np.exp(np.cos(theta))-2*np.cos(4*theta)-np.sin(theta/12)**5)
y=np.cos(theta)*(np.exp(np.cos(theta))-2*np.cos(4*theta)-np.sin(theta/12)**5)
plt.plot(x,y,'b')
plt.title("Fey's function")
plt.ylabel("y")
plt.xlabel("x")
plt.show()