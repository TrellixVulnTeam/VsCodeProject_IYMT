'''
-------------------------------------------------------------------------
matplotlib.contour



-------------------------------------------------------------------------
'''
# common library
import os, sys
from pathlib import Path

import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

print   (
        '------------------------------------------------------------------------------------------------------\n'
        '       Example 1 ( meshgrid and contour)                                                              \n'
        '------------------------------------------------------------------------------------------------------\n'
        )

# create mesh data
delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

# Create a simple contour plot with labels using default colors. 
# The inline argument to clabel will control whether the labels are draw over the line segments of the contour, 
# removing the lines beneath the label

# 3D plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z, linewidth=0.2, antialiased=True)
ax.set_
ax.set_title('3d surface')
plt.show()


fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=1, fontsize=10)
ax.set_title('Simplest default with labels')
plt.show()

# contour labels can be placed manually by providing list of positions (in data coordinate). 
# See ginput_manual_clabel.py for interactive placement.
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
manual_locations = [(-1, -1.4), (-0.62, -0.7), (-2, 0.5), (1.7, 1.2), (2.0, 1.4), (2.4, 1.7)]
ax.clabel(CS, inline=1, fontsize=10, manual=manual_locations)
ax.set_title('labels at selected locations')
plt.show()

# You can force all the contours to be the same color.
fig, ax = plt.subplots()
CS = ax.contour(
                    X, Y, Z, 6,
                    colors='k',  # negative contours will be dashed by default
                )
ax.clabel(CS, fontsize=9, inline=1)
ax.set_title('Single color - negative contours dashed')
plt.show()

# You can set negative contours to be solid instead of dashed:
matplotlib.rcParams['contour.negative_linestyle'] = 'solid'
fig, ax = plt.subplots()
CS = ax.contour(
                    X, Y, Z, 6,
                    colors='k',  # negative contours will be dashed by default
                )
ax.clabel(CS, fontsize=9, inline=1)
ax.set_title('Single color - negative contours solid')

# And you can manually specify the colors of the contour
fig, ax = plt.subplots()
CS = ax.contour(
                    X, Y, Z, 6,
                    linewidths=np.arange(.5, 4, .5),
                    colors=('r', 'green', 'blue', (1, 1, 0), '#afeeee', '0.5')
                )
ax.clabel(CS, fontsize=9, inline=1)
ax.set_title('Crazy lines')

# Or you can use a colormap to specify the colors; the default colormap will be used for the contour lines
fig, ax = plt.subplots()
im = ax.imshow(
                Z, 
                interpolation='bilinear', 
                origin='lower',
                cmap=cm.gray, 
                extent=(-3, 3, -2, 2)
            )

levels = np.arange(-1.2, 1.6, 0.2)
CS = ax.contour(
                    Z, 
                    levels, 
                    origin='lower', 
                    cmap='flag',
                    linewidths=2, 
                    extent=(-3, 3, -2, 2)
                )

# Thicken the zero contour.
zc = CS.collections[6]
plt.setp(zc, linewidth=4)

ax.clabel(
            CS, 
            levels[1::2],  # label every second level
            inline=1, 
            fmt='%1.1f', 
            fontsize=14
        )

# make a colorbar for the contour lines
CB = fig.colorbar(CS, shrink=0.8, extend='both')

ax.set_title('Lines with colorbar')

# We can still add a colorbar for the image, too.
CBI = fig.colorbar(im, orientation='horizontal', shrink=0.8)

# This makes the original colorbar look a bit out of place,
# so let's improve its position.

l, b, w, h = ax.get_position().bounds
ll, bb, ww, hh = CB.ax.get_position().bounds
CB.ax.set_position([ll, b + 0.1*h, ww, h*0.8])

plt.show()