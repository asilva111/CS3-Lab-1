# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 15:37:30 2019

    This program will draw concentric circles in defined positions, more specifically, 5 circles inside each ciricle.
Those circles contain one third of the radius of the previous circle. The recursive method draw_circles calls itself 5 different times
(one for each circle) but each call with different parameters: reduced radius, and shifted centers (except the center circle, which will always
have the same center).

@author: Andres Silva
"""

import matplotlib.pyplot as plt
import numpy as np
import math 

def circle(center,rad): #Model code stays unmodified, it just traces a circle with a center and a radius.
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

#The following method will create 5 circles each iteration after the first one.
def draw_circles(ax,n,center,radius,w): #It will take an axis to draw on, n - depth of recursion, a center, radius, and a scaling factor.
    if n>0:
        x,y = circle(center,radius) 
        ax.plot(x,y,color='k') #Plot the circle.
        draw_circles(ax,n-1,center, radius *w, w ) #Draw a circle at the same center than the previous one (Center circle), but with a third (w) of the radius.
        draw_circles(ax,n-1,[center[0] + radius*2*w, center[1]], radius *w, w ) #Call to draw a circle with a shifted center by 2/3 to the right with a third of the radius.
        draw_circles(ax,n-1,[center[0] - radius*2*w, center[1]], radius *w, w ) #Call to draw a circle with a shifted center by 2/3 to the left with a third of the radius.
        draw_circles(ax,n-1,[center[0], center[1] + radius*2*w], radius *w, w ) #Call to draw a circle with a shifted center by 2/3 up with a third of the radius.
        draw_circles(ax,n-1,[center[0], center[1] - radius*2*w], radius *w, w ) #Call to draw a circle with a shifted center by 2/3 down with a third of the radius.

plt.close("all") 
fig, ax = plt.subplots() 


draw_circles(ax,4,[0,0],1000,1/3) 
#draw_circles(ax,3,[0,0],1000,1/3)
#draw_circles(ax,5,[0,0],1000,1/3)


ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles3.png')