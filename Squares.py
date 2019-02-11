# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 19:08:35 2019

@author: Andres Silva
    This recursive method will draw a square at a given center with a given 'radius', it then will draw a square in each of the corners
of the previously drawn square. This is accomplished by having a method that plots a square given a center and a radius.
This method will calculate the corners of the square by adding and substracting the radius to the center.

    The recursive part of the method stores the coordinates of the corners into points and calls itself with those corners for a center.    
"""
import matplotlib.pyplot as plt

#Here we have a method that will draw a square with a provided center and radius.
#The method calculates the 4 points of the square by substracting or adding the radius to the center. 
#The method will then plot straight lines between those corners.

def square(ax,center,radius): #Format: [X1,X2],[Y1,Y2]
    ax.plot([center[0] + radius, center[0] + radius], [center[1] + radius, center[1] - radius],color='k') #[r,r] to [r,-r].
    ax.plot([center[0] + radius, center[0] - radius], [center[1] - radius, center[1] - radius],color='k') #[r,-r] to [-r,-r].
    ax.plot([center[0] - radius, center[0] - radius], [center[1] - radius, center[1] + radius],color='k') #[-r,-r] to [-r,r].
    ax.plot([center[0] - radius, center[0] + radius], [center[1] + radius, center[1] + radius],color='k') #[-r,r] to [r,r].

def draw_squares(ax,n,center,radius):
    if n>0: 
        square(ax,center,radius) #Draw a square with the given parameters.
        p1 = [center[0] + radius, center[1] + radius] #Store Point one (or corner one) in p1 - [r,r].
        p2 = [center[0] + radius, center[1] - radius] #Store Point two (or corner two) in p1 - [r,-r].
        p3 = [center[0] - radius, center[1] + radius] #Store Point three (or corner three) in p1 - [-r,r].
        p4 = [center[0] - radius, center[1] - radius] #Store Point four (or corner four) in p1 - [-r,-r].
        
        draw_squares(ax,n-1,p1,radius/2) #Use each of the previous corners as centers for new squares with half the radius.
        draw_squares(ax,n-1,p2,radius/2) 
        draw_squares(ax,n-1,p3,radius/2)
        draw_squares(ax,n-1,p4,radius/2)

       
plt.close("all")
fig, ax = plt.subplots()#Call method below this line.

draw_squares(ax,4,[0,0],100)

ax.set_aspect(1.0) #And before this one.
ax.axis('off')
plt.show()
fig.savefig('squares.png')
