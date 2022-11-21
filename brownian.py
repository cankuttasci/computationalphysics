#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 14:49:28 2022

@author: cankuttasci
"""
import numpy as np
import matplotlib.pyplot as plt
import random

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

fig = plt.figure()
plts = []
    # [0, 0, 0, ... ,0]
n = 100
x = np.zeros(n)
y = np.zeros(n)
x[0]=50
y[0]=50
directions = ["UP", "DOWN", "LEFT", "RIGHT"]
for i in range(1, n):
    # Pick a direction at random
    step = random.choice(directions)
    
    # Move the object according to the direction
    if step == "RIGHT":
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
    elif step == "LEFT":
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif step == "UP":
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    elif step == "DOWN":
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1
    
    # Return all the x and y positions of the object
    
    plts.append(plt.plot(x[:i], y[:i]))
    
ani = animation.ArtistAnimation(fig, plts, interval=50, blit=True,
                                repeat_delay=500)

writer = PillowWriter(fps=20)
ani.save("brownian.gif", writer='imagemagick')
