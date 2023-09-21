# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 00:03:58 2023

@author: adrian
"""

import matplotlib.pyplot as plt
import numpy as np
import re


#Open file created by logisticRegressionXG.py
#If file does not exist (running for the first time), then run logisticRegressionXG.py FIRST

with open("shotDistanceModel.txt") as coef:
    lines = coef.readlines()

#Extract coefficients (that have previously been written to the .txt file in logisticRegressionXG.py) 

def extractDistance():
    pattern = r"coef_ShotDistance:\s+(-?\d+\.\d+)"
    for line in lines:
        match = re.search(pattern, line)
        if match:
            coef_ShotDistance = match.group(1)
            coef_ShotDistance = float(coef_ShotDistance)
            print("Distance: " + str(coef_ShotDistance))
    return (coef_ShotDistance)
        
def extractIntercept():
    pattern_2 = r"coef_D_Intercept:\s+(-?\d+\.\d+)"       
    for line in lines:
        match = re.search(pattern_2, line)
        if match:
            coef_D_Intercept = match.group(1)
            coef_D_Intercept = float(coef_D_Intercept)
            print("Intercept: " + str(coef_D_Intercept))
    return (coef_D_Intercept)


#Plot Logistic Regression Curve
def equation(x):
    return (1 / (1 + np.exp(extractIntercept() + extractDistance()*x) ))

x = np.linspace(0, 100, 100)  
y = equation(x)

plt.plot(x, y, label='Logistic Regression Curve')
plt.xlabel('Shot Distance (m)')
plt.ylabel('Probability of Goal')
plt.title('Shot Distance Logistic Regression Model')


plt.legend()
plt.grid(False)
plt.show()