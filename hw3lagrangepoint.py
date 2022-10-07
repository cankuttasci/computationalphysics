#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 17:43:04 2022

@author: cankuttasci
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import *
def func(x):
    w=2.662*10**-6
    m=7.348*10**22
    G=6.6743*10**-11
    M=5.972*10**24
    R=3.844*10**8
    return (w**2)*x**5-2*(w**2)*R*x**4+(w**2)*(R**2)*x**3+(G*m-G*M)*x**2+2*G*M*R*x-G*M*(R**2)
w=2.662*10**-6
m=7.348*10**22
G=6.6743*10**-11
M=5.972*10**24
R=3.844*10**8
x=symbols('x')
f=(w**2)*x**5-2*(w**2)*R*x**4+(w**2)*(R**2)*x**3+(G*m-G*M)*x**2+2*G*M*R*x-G*M*(R**2)
y=diff(f)
def dfunc(z):
    return y.subs(x,z)
i=0
x0=10**8
while i<1000:
    if np.abs(x0-(x0-func(x0)/(dfunc(x0))))<10**-4:
        break
    x0=x0-func(x0)/(dfunc(x0))
    i=i+1
d=np.linspace(10**8,0.5*10**9,100)
plt.plot(d,func(d))
plt.show()                    
print(x0)
print(func(x0))   