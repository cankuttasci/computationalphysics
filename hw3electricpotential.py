#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 20:58:36 2022

@author: cankuttasci
"""
import numpy as np
import matplotlib.pyplot as plt
x1,y1,z1=-0.05,0,0
x2,y2,z2=0.05,0,0
e0=8.854*10**(-12)
#k=1/(4*np.pi*e0)
k=1
z=0
xx=np.linspace(-0.499,0.499,100)
yy=np.linspace(-0.499,0.499,100)
x,y=np.meshgrid(xx,yy)
z2=-k/(np.sqrt((x-x1)**2+(y-y1)**2+(z-z1)**2))+k/(np.sqrt((x-x2)**2+(y-y2)**2+(z-z2)**2))
fig,ax2 = plt.subplots(1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Density of Electric Potential')
ax2.contourf(x,y,z2)
plt.show()
