#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 16:34:09 2022

@author: cankuttasci
"""

import numpy as np
import random as random
import sys
def f(x):
    return 1/(np.exp(x)+1)
N=1000000
Value=0
def inverse(x):
    return x**2
def p(x):
    return 1/(2*np.sqrt(x))
for i in range(N):
    x=random.uniform(0,1)
    y=inverse(x)
    Value+=(f(y))
result=2*Value/N
print(result)