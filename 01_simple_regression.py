# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 21:41:03 2021

@author: sundh
"""

import matplotlib.pyplot as plt

x = [[6],[8],[10],[14],[18],[21]]
y = [[7],[9],[13],[17.5],[18],[24]]

plt.figure()
plt.title('Pizza price statics problem')
plt.xlabel('Diameter (inches)')
plt.ylabel('Price (dollars)')
plt.plot(x,y,'.')
plt.axis([0,25,0,25])
plt.grid(True)
plt.show()