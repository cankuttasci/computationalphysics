# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np
theta=np.linspace(0,2*np.pi,100)
x=2*np.cos(theta)+np.cos(2*theta)
y=2*np.sin(theta)-np.sin(2*theta)
plt.plot(x,y,'b')
plt.title("Deltoid Curve")
plt.ylabel("y")
plt.xlabel("x")
plt.show()