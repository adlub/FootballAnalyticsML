# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 19:18:54 2023

@author: adrian
"""

import matplotlib.pyplot as plt
import numpy as np
import re

#Open file created by logisticRegressionXG.py
#If file does not exist (running for the first time), then run logisticRegressionXG.py FIRST

with open("shotAngleModel.txt") as coef:
    lines = coef.readlines()
    
    
#Extract coefficients (that have previously been written to the .txt file in logisticRegressionXG.py) 
    
def extractAngle():
    pattern = r"coef_ShotAngle:\s+(-?\d+\.\d+)"
    for line in lines:
        match = re.search(pattern, line)
        if match:
            # Extract the number from the matched pattern
            coef_ShotAngle = match.group(1)
            # Convert the extracted string to a float
            coef_ShotAngle = float(coef_ShotAngle)
            # Print the retrieved number
            print("Angle: " + str(coef_ShotAngle))
    return (coef_ShotAngle)
        
def extractIntercept():
    pattern_2 = r"coef_SA_intercept:\s+(-?\d+\.\d+)"       
    for line in lines:
        match = re.search(pattern_2, line)
        if match:
            # Extract the number from the matched pattern
            coef_SA_intercept = match.group(1)
            # Convert the extracted string to a float
            coef_SA_intercept = float(coef_SA_intercept)
            # Print the retrieved number
            print("Intercept: " + str(coef_SA_intercept))
    return (coef_SA_intercept)

#Plot Logistic Regression Curve
def equation(x):
    return (1 / (1 + np.exp(extractIntercept() + extractAngle()*x)))

x = np.linspace(-100, 150, 100)  
y = equation(x)

plt.plot(x, y, label='Logistic Regression Curve')
plt.xlabel('Shot Angle (Degrees)')
plt.ylabel('Probability of Goal')
plt.title('Shot Angle Logistic Regression Model')


plt.legend()
plt.grid(False)
plt.show()

