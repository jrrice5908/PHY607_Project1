## ODE

import numpy as np
import matplotlib.pyplot as plt

def update(I,charge,step,T):
    Qnew = np.add(Q, I*step)
    Inew = np.add(I, -Qnew/T)
    

V = 100     #some initial potential
R = 10      #some resistance
C = 15      #some capacitance
T = R + C   #time constant

I = np.array(0.05)
charge = np.array(0)     #initial charge Q(0)=0
step = 0.001
Q = []

for i in range(100000):                              #EXPLICIT
    I, charge = update(I,charge,step,T)
    Q.append(charge)
t = np.arange(len(x))*step

plt.plot(t,x)
plt.ylabel('Q, coulombs')
plt.xlabel('time, seconds')
plt.show


# Please enter the commit message for your changes. Lines starting
