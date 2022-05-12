import numpy as np
import matplotlib.pyplot as plt

def wiener_process(T, N):
	W0 = [1]
	dt = T/float(N)
	increments = np.random.normal(0, 1*np.sqrt(dt), N)
	W = W0+list(np.cumsum(increments))
	return W

N = 1000
T = 10
dt = T / float(N)
t = np.linspace(0.0, N*dt, N+1)
plt.figure(figsize=(15,10))
for i in range(10):
    W = wiener_process(T, N)
    plt.plot(t, W)
    plt.xlabel('time')
    plt.ylabel('Price')
    plt.grid(True)
    
plt.show()