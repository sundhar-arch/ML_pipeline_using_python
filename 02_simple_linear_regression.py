# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 22:24:38 2021

@author: sundh
"""

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


x = [[6],[8],[10],[14],[18],[21]]
y = [[7],[9],[13],[17.5],[18],[24]]

model = LinearRegression()
model.fit(x,y)

plt.figure()
plt.title('Pizza price statics problem')
plt.xlabel('Diameter (inches)')
plt.ylabel('Price (dollars)')
plt.plot(x,y,'.')
plt.axis([0,25,0,25])
plt.grid(True)
plt.show()

print("Predicted price = ",model.predict([[21]]))
# output  Predicted price =  [[23.31436837]]
