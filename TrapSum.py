## Trapezoidal Rule

import numpy as np
import matplotlib.pyplot as plt

def ChargeDist(x,y,z):
    charge = (4*C/(a**4))*((x*z)/(y+a)**2)
    return charge

xmin = 0
xmax = 20                       

ymin = 0
ymax = 30                       
                         
zmin = 0
zmax = 50                       
                         
a = 10
C = 1

totCharge = 0    
    
for i in range(xmin,xmax,step_vol):
        for j in range(ymin,ymax,step_vol):
            for k in range(zmin,zmax,step_vol):
                pointCharge = ((ChargeDist(i-1,j-1,k-1)+ChargeDist(i,j,k))/2)*step_vol
                totCharge = totCharge + pointCharge    
    
    
print ("Total Charge = ",totCharge)
