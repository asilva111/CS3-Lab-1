# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 16:02:35 2019

@author: Andres Silva
    This program will draw tree like structures depending of the levels (n) provided. Each segment vertically is of the same length.
Each center point has 2 children, and each children has 2 children.

    We start by having a method that draws 2 lines between 3 provided points, which we will refer to as center, p1, p2.
The recursive method, draw_trees will calculate the position of the child points by adding and substracting to the center coordinate.
The values that modify the center coordinates depend on the desired height and width of each branch of the tree (which are defined
by the user in the parameters of the method). It then will call the drawing method twice, each with a a child for the new center.

   The branches of the tree will always be drawn downwards, so the Y coordinate of every point will decrease (by a constant value to keep 
all the distances between centers the same). The case is not the same for the X coordinates because there is the left and right side, so 
depending on to which side the center must be moved, the program will add or subtract.            

    The width of the tree decreases with each iteraion, so it was noted that while the center moves by half the distance from the point to the
center, the children then moved by half of that distance again, hence the '/4' on the new coordinates of each new p1 and p2.                                                                                     
"""

import matplotlib.pyplot as plt


#This is a method that will draw 2 lines between 3 given points.
#The method will use a center and plot lines between it and two other lower points to make an inverted V.
def lines(ax,center,p1,p2): 
    ax.plot([center[0],p1[0]],[center[1],p1[1]] ,color='k')#Format: [X1,X2],[Y1,Y2]
    ax.plot([center[0],p2[0]],[center[1],p2[1]] ,color='k')


#The following method will take an ax, n times to do recursion, "segment_height" (which is how tall each level of the tree will be, and a "segment_width" (which is the defined width of the tree)).
def draw_trees(ax,n,center,segment_height,segment_width): 
    if n>0:
       #The following children points are calculated relative to the center. They will always be segment_height-tall and segment_width on the X axis.
        p1 =[center[0] - segment_width/4 ,center[1] - segment_height] #The two children points are calculated and stored in point 1 (p1) and point 2 (p2).
        p2 =[center[0] + segment_width/4 ,center[1] - segment_height] #Note how the X coordinate of the point becomes smaller each iteration, and how the Y coordinate decreases by a constant value.
        
        lines(ax,center,p1,p2) #With those points calculated, we call the lines method to simply draw lines between those calculated points.
    
        #Now we have a recursive call for each child point.       
        draw_trees(ax,n-1,p1,segment_height, segment_width/2) #Each of the previous points now becomes a center, which will have two more children.
        draw_trees(ax,n-1,p2,segment_height, segment_width/2) #Note how n will stop recursion, how the center is now a point previously calculated, how the segment_height stays constant, and the width decreases even more.
        

plt.close("all")
fig, ax = plt.subplots()#Call method below this line.

draw_trees(ax,6,[0,0],1000,5000) #Run it with 3,4 for n and 3000 - then run it with n = 6, but last parameter 5000 just for better detail.
#lines(ax,[0,0],[-500,-1000],[500,-1000]).

ax.set_aspect(1.0) #And before this one .
ax.axis('off')
plt.show()
fig.savefig('trees.png')