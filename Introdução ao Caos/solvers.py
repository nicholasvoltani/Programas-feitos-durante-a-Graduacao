import numpy as np

def Euler(t,dt,vars,params,funcs):
    update = np.array([f(t,*vars,*params) for f in funcs])
    return vars + update*dt

def RK4(t,dt,vars,params,funcs):
    k1 = np.array([f(t,*vars,*params) for f in funcs])
    k2 = np.array([f(t+dt/2,*(vars+k1*dt/2),*params) for f in funcs])
    k3 = np.array([f(t+dt/2,*(vars+k2*dt/2),*params) for f in funcs])
    k4 = np.array([f(t+dt,*(vars+dt*k3),*params) for f in funcs])
    return vars + (dt/6)*(k1 + 2*k2+2*k3+k4)
