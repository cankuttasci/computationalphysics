# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt


def error(y):
  def myfunc(x):
      return np.exp(-x**2)

  l=y
  N=30000
  delta=l/N
  h=myfunc(0)+myfunc(2)    
  j=1
  i=1
  s=0
  p=0
  while j<N/2:
    p+=myfunc(2*j*delta)
    j+=1
  while i<N/2+1:
    s+=myfunc((2*i-1)*delta)
    i+=1
  return delta/3*(h+4*s+2*p) 
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
x=np.linspace(-5,5,1000)
plt.xlabel('x')
plt.title('E(x) vs x')
plt.plot(x,error(x))
plt.grid()
plt.show()