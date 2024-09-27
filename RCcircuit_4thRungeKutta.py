# ODE Runge-Kutta

import numpy as np
import matplotlib.pyplot as plt

def r_update(charge,step,T):
    k1 = -((charge)/T)*step
    k2 = -(charge)+(k1*(step/2))
    k3 = -(charge)+(k2*(step/2))
    k4 = -(charge)+(k3*(step))
    Qnew = np.add(charge,((k1/6)+(k2/3)+(k3/3)+(k4/6))*step)
    return Qnew
  
R = 30		#Ohms     
C = 5      	#Farrads
T = R + C  	#Time Constant

charge = np.array([10])     
step = 0.001
Q = []

for i in range(100000):                              
    charge = r_update(charge,step,T)
    Q.append(charge)
t = np.arange(len(Q))*step



plt.plot(t,Q)
plt.ylabel('Q, coulombs')
plt.xlabel('time, seconds')
plt.title("Charge on capacitor vs Time")
plt.show
plt.savefig("ChargevsTimeRungeKuttaAlternate.png")
