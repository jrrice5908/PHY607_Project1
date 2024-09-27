# ODE, Euler's Method

import numpy as np
import matplotlib.pyplot as plt

def update(charge,step,T):
    Qnew = np.add(charge,-(charge/T)*step)
    return Qnew
        
R = 10
C = 15     
T = R + C  

charge = np.array([1])    
step = 0.001
Q = []

for i in range(100000):                             
    charge = update(charge, step, T)
    Q.append(charge)
t = np.arange(len(Q))*step

plt.plot(t, Q)
plt.ylabel('Q, coulombs')
plt.xlabel('time, seconds')
plt.title("Charge on Capacitor vs Time")
plt.show

plt.savefig("ChargevsTimeEuler.png")
