## Integral Reimann Sum

import numpy as np
import matplotlib.pyplot as plt

def ChargeDist(x,y,z):
    charge = (4*C/(a**4))*((x*z)/(y+a)**2)
    return charge
   
                   
step_vol = 1

xmin = 0
xmax = 20                       

ymin = 0
ymax = 30                       
                         
zmin = 0
zmax = 50                       
                         
a = 10
C = 1

totCharge = 0

for i in range(xmin,xmax):
        for j in range(ymin,ymax):
            for k in range(zmin,zmax):
                pointCharge = ChargeDist(i,j,k)*step_vol
                totCharge = totCharge + pointCharge
        
print (totCharge)
