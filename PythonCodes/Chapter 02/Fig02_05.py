
import numpy as np
import matplotlib.pyplot as plt

def genGBM(NPaths,NSteps,T,r,sigma,S_0):    
    Z = np.random.normal(0.0,1.0,[NPaths,NSteps])
    X = np.zeros([NPaths, NSteps+1])
    S = np.zeros([NPaths, NSteps+1])
    time = np.zeros([NSteps+1])
        
    X[:,0] = np.log(S_0)
    
    dt = T / float(NSteps)
    for i in range(0,NSteps):


        if NPaths > 1:
            Z[:,i] = (Z[:,i] - np.mean(Z[:,i])) / np.std(Z[:,i])
     
        X[:,i+1] = X[:,i] + (r - 0.5 * sigma * sigma) * dt + sigma *\
        np.power(dt, 0.5)*Z[:,i]
        time[i+1] = time[i] +dt


    S = np.exp(X)
    paths = {"time":time,"S":S}
    return paths
    
def simulation():
    NPaths = 10
    NSteps = 10000
    S_0       = 1
    r         = 0.05
    mu        = 0.15
    sigma     = 0.1
    T         = 10

  

    M         = lambda t: np.exp(r * t)
    

    pathsQ    = genGBM(NPaths,NSteps,T,r,sigma,S_0)
    S_Q       = pathsQ["S"]
    pathsP = genGBM(NPaths,NSteps,T,mu,sigma,S_0)
    S_P = pathsP["S"]
    time= pathsQ["time"]    


    S_Qdisc = np.zeros([NPaths,NSteps+1])
    S_Pdisc = np.zeros([NPaths,NSteps+1])
    i = 0
    for i, ti in enumerate(time):
        S_Qdisc[:, i] = S_Q[:,i]/M(ti) 
        S_Pdisc[:, i] = S_P[:,i]/M(ti) 
    


    plt.figure(1)
    plt.grid()
    plt.xlabel("time")
    plt.ylabel("S(t)")
    eSM_Q = lambda t: S_0 * np.exp(r *t) / M(t)
    plt.plot(time,eSM_Q(time),'r--')
    plt.plot(time, np.transpose(S_Qdisc),'green')
    plt.legend(['E^Q[S(t)/M(t)]','paths S(t)/M(t)'])
    
  

    plt.figure(2)
    plt.grid()
    plt.xlabel("time")
    plt.ylabel("S(t)")
    eSM_P = lambda t: S_0 * np.exp(mu *t) / M(t)
    plt.plot(time,eSM_P(time),'r--')
    plt.plot(time, np.transpose(S_Pdisc),'green')
    plt.legend(['E^P[S(t)/M(t)]','paths S(t)/M(t)'])
    
simulation()
plt.show()