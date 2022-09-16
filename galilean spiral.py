# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 08:15:53 2022

@author: 90537
"""

import matplotlib.pyplot as plt
import numpy as np
theta=np.linspace(0,10*np.pi,100)
x=(theta**2)*np.cos(theta)
y=(theta**2)*np.sin(theta)
plt.plot(x,y,'b')
plt.title("Galilean spiral")
plt.ylabel("y")
plt.xlabel("x")
plt.show()