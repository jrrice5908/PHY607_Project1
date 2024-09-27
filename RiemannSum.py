# Integral Reimann Sum

import numpy as np
import matplotlib.pyplot as plt

def ChargeDist(x,y,z):		#This is a three dimensional volume charge distribution in certesian coordinates			
    charge = (4*C/(a**4))*((x*z)/(y+a)**2)
    return charge
                      
step_vol = 1			#This is analogous to step size in spherical cow problem, all values are in cm 

xmin = 0
xmax = 20                       

ymin = 0
ymax = 30                       
                         
zmin = 0
zmax = 50                       

tot_vol=(xmax-xmin)*(ymax-ymin)*(zmax-zmin)                         
a = 10				#Artbitray constants 
C = 1

totCharge = 0			#Giving charge an initial value such that I can call it in following algorithm, total charge given by Coulombs

for i in range(xmin, xmax, step_vol):
        for j in range(ymin, ymax, step_vol):
            for k in range(zmin, zmax, step_vol):
                pointCharge = ChargeDist(i, j, k)*step_vol
                totCharge = totCharge + pointCharge
        
print ("Total Charge = ", totCharge, "C", "across total volume,", tot_vol, "cm^3")

#Different Initial Conditions

xmin = 0
xmax = 64

ymin = 0
ymax = 72

zmin = 0
zmax = 30

tot_vol=(xmax-xmin)*(ymax-ymin)*(zmax-zmin)
a = 10                          #Artbitray constants 
C = 1

totCharge = 0                   #Giving charge an initial value such that I can call it in following algorithm, total charge given by Coulombs

for i in range(xmin, xmax, step_vol):
        for j in range(ymin, ymax, step_vol):
            for k in range(zmin, zmax, step_vol):
                pointCharge = ChargeDist(i, j, k)*step_vol
                totCharge = totCharge + pointCharge

print ("Total Charge = ", totCharge, "C", "across total volume,", tot_vol, "cm^3")




