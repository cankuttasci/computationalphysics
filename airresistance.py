#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 18:07:34 2022

@author: cankuttasci
"""

import numpy as np

import matplotlib.pyplot as plt

def fy(y):
    return y
def fx(x):
    return x
def fX(x,y,R,m,rho,C):
    return -(np.pi*R**2*rho*C)/(2*m)*x*np.sqrt(x**2+y**2)
def fY(x,y,R,m,rho,C):
    return -9.8-(np.pi*R**2*rho*C)/(2*m)*y*np.sqrt(x**2+y**2)
#time interval
deltat=0.5
h=0.5
t0=0
t=[]
x=[]
y=[]
Xar=[]
Yar=[]
v=100
X0=v*np.cos(np.deg2rad(30))
Y0=v*np.sin(np.deg2rad(30))
x0,y0=0,0
x.append(x0)
y.append(y0)
R=0.08
C=0.47
rho=1.22
i=0
X=X0
Y=Y0
Xar.append(X0)
Yar.append(Y0)
t.append(t0)
mar=[0.3,0.5,1,5,10]
Range=[]
for m in mar:
   while t0<8: 
    t0+=deltat
    R=0.08
    C=0.47
    rho=1.22
    X=Xar[i]
    Y=Yar[i]
    k1Y = deltat*fX(X,Y,R,m,rho,C)
    k2Y = deltat*fX(X+0.5*k1Y,Y+0.5*k1Y,R,m,rho,C) 
    k3Y = deltat*fX(X+0.5*k2Y,Y+0.5*k2Y,R,m,rho,C) 
    k4Y = deltat*fX(X+k3Y,Y+k3Y,R,m,rho,C)
    k1X = deltat*fX(X,Y,R,m,rho,C)
    k2X = deltat*fX(X+0.5*k1X,Y+0.5*k1X,R,m,rho,C) 
    k3X = deltat*fX(X+0.5*k2X,Y+0.5*k1X,R,m,rho,C) 
    k4X = deltat*fX(X+k3X,Y+k3X,R,m,rho,C)
    X +=(k1X+2*k2X+2*k3X+k4X)/6
    Y +=(k1Y+2*k2Y+2*k3Y+k4Y)/6
    Xar.append(X)
    Yar.append(Y)
    i+=1
    t.append(t0)
   for j in range(np.size(t)):
    x0+=deltat*Xar[j]
    y0+=deltat*Yar[j]
    x.append(x0)
    y.append(y0)
   Range.append(x[-1])

print(Range)
plt.plot(mar,Range)
plt.xlabel('mass(kg)')
plt.ylabel('Range(m)')
plt.title('Range vs mass relation')
