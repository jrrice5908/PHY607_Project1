## ODE

import numpy as np
import matplotlib.pyplot as plt

def update(I,charge,step,T):
    Qnew = np.add(charge, I*step)
    #Inew = np.add(I, -Qnew/T)
    return Qnew
    

V = 100     #some initial potential
R = 10      #some resistance
C = 15      #some capacitance
T = R + C   #time constant

I = np.array([0.05])
charge = np.array([0])     #initial charge Q(0)=0
step = 0.001
Q = []

for i in range(100000):                              #EXPLICIT
    charge = update(I,charge,step,T)
    Q.append(charge)
t = np.arange(len(Q))*step

plt.plot(t,Q)
plt.ylabel('Q, coulombs')
plt.xlabel('time, seconds')
plt.show
