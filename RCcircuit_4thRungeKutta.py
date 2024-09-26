## ODE Runge-Kutta

import numpy as np
import matplotlib.pyplot as plt



def update(charge,step,T):
    Qnew = np.add(charge,-(charge/T)*step)
    return Qnew

def rk():
    k1 = -(charge/T)
    k2 = 
    return 


V = 100    
R = 10     
C = 15      
T = R + C  

charge = np.array([1])     
step = 0.001
Q = []
k = []

for i in range(100000):                              
    charge = update(charge,step,T)
    Q.append(charge)
t = np.arange(len(Q))*step
