import numpy as np

K1=10**8
K_1=10**(-4)
K2=10**(-6)
K3=10**8
K_3=10**(-4)
K4=10**(-6)
Km1=(K_1+K2)/K1
Km2=(K_3+K4)/K3
sod_total=0.00005
sod_low=0.00001
sod_high=0.00001
ros = np.linspace(0, 100)
dvn1max=-2
dvnmax=3
dkn1m=15
dknm=13