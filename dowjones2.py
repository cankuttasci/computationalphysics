#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 17:34:23 2022

@author: cankuttasci
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import fft
with open('dow2.txt') as file:
    lines = file.readlines()
for i in range(len(lines)):
   lines[i]=lines[i].replace('\n','')
   lines[i]=float(lines[i])
N=len(lines)
x1=list(range(0,N))
dft2=np.fft.rfft(lines)
dft1=np.fft.rfft(lines)
print(dft1)
N3=len(dft1)
dft=np.fft.rfft(lines)
dftsort=np.sort(dft)
dftindex=np.argsort(dft)
N1=len(dft)
i=0
while i<N1:
    if i>500:
        x=dftindex[i]
        dft2[x]=dft2[x]
    if i>462:
        x=dftindex[i]
        dft[x]=dft[x]
    if i<462:
        x=dftindex[i]
        dft[x]=0
    if i<500:
        x=dftindex[i]
        dft2[x]=0
    i+=1
inversedft=np.fft.irfft(dft)
inversedft2=np.fft.irfft(dft2)
N2=len(inversedft)
x2=list(range(0,N1))
x3=list(range(0,N3))
plt.title('Exercise 7.6')
plt.plot(x1,lines,'g-',label='without filter')
#plt.plot(x1,inversedft,'b-',label='90%=0')
plt.plot(x1,inversedft2,'r-',label='98%=0')
plt.legend()
#print(x3,dft1)