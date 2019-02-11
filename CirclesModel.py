# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 13:47:12 2019

@author: Andres Silva
    This program will recursively draw concentric circles with a decreasing radius and a shifting to the left center.
This is accomplished by shifting the center of the each circle by a defined percentage, along with the radius.
"""

import matplotlib.pyplot as plt
import numpy as np
import math 

def circle(center,rad): #Model code without modification.
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y


def draw_circles(ax,n,center,radius,w): #This method takes the axis to draw on, level of recursion, circle radius, and a factor to scale (reduce) by.
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        draw_circles(ax,n-1,[radius*w ,0],radius*w,w ) #This recursive call will call itself with n-1 (to advance), an X coordinate shifted to the left by w, a reduced radius, and the same reduction factor.

    
plt.close("all") 
fig, ax = plt.subplots() 

#draw_circles(ax, 100, [100,0], 100,.6) #Here we call the "main" method with different values to produce different figures.

draw_circles(ax, 100, [100,0], 100,.9) #An scaling factor closer to one will produce circles closer to the original size each iteration.

#draw_circles(ax, 100, [100,0], 100,.95).

ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles.png')