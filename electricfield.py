#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 21:07:21 2022

@author: cankuttasci
"""
# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff
 
 
# Creating arrows
x1,y1,z1=-0.05,0,0
x2,y2,z2=0.05,0,0
e0=8.854*10**(-12)
#k=1/(4*np.pi*e0)
k=1
z=0
xx1=np.linspace(-0.4,-0.01,10)
xx2=np.linspace(0.01,0.4,10)
xxx=np.concatenate([xx1,xx2])
yy1=np.linspace(-0.4,-0.01,10)
yy2=np.linspace(0.1,0.4,10)
yyy=np.concatenate([yy1,yy2])
xx=np.linspace(-0.4,0.4,10)
yy=np.linspace(-0.4,0.4,10)
#print(xxx,xx)
# Creating gradient
x, y = np.meshgrid(xx, yy)
xt,yt= np.meshgrid(xx,yy)
#z2=-k/(np.sqrt((x-x1)**2+(y-y1)**2+(z-z1)**2))+k/(np.sqrt((x-x2)**2+(y-y2)**2+(z-z2)**2))
z2=k/(np.sqrt((x-x1)**2+(y-y1)**2))+k/(np.sqrt((x-x2)**2+(y-y2)**2))
#dx=diff(z2,x)
#dy=diff(z2,y)
# Creating plot
dx,dy = np.gradient(-z2)
cond1 = np.abs(dx)>10**-2
cond2 = np.abs(dy)>10**-2
i=0
while i<10:
      j=0
      while j<10:
          if np.abs(dx[i,j])<10**(-1):
              print(i,j,dx[i,j],x[i,j],y[i,j])
          j+=1
      i+=1
fig, ax = plt.subplots(figsize =(8, 8))
ax.quiver(x, y, dx, dy)
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.set_aspect('equal')
plt.show()
