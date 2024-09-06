import numpy as np
from variables import k_ROS,k_deg ,k_SOD ,K_ROS ,n ,ROS_0,T,dt,steps

ROS_rk4 = np.zeros(steps)
SOD_rk4 = np.zeros(steps)
time = np.linspace(0, T, steps)

ROS_rk4[0] = ROS_0


#Runge–Kutta (RK4) iteration
for i in range(1, steps):
    # Calculate the four slopes
    SOD1 = k_SOD * (ROS_rk4[i - 1] ** n) / (K_ROS ** n + ROS_rk4[i - 1] ** n)
    k1 = dt * (k_ROS - k_deg * SOD1 * ROS_rk4[i - 1])

    SOD2 = k_SOD * ((ROS_rk4[i - 1] + 0.5 * k1) ** n) / (K_ROS ** n + (ROS_rk4[i - 1] + 0.5 * k1) ** n)
    k2 = dt * (k_ROS - k_deg * SOD2 * (ROS_rk4[i - 1] + 0.5 * k1))

    SOD3 = k_SOD * ((ROS_rk4[i - 1] + 0.5 * k2) ** n) / (K_ROS ** n + (ROS_rk4[i - 1] + 0.5 * k2) ** n)
    k3 = dt * (k_ROS - k_deg * SOD3 * (ROS_rk4[i - 1] + 0.5 * k2))

    SOD4 = k_SOD * ((ROS_rk4[i - 1] + k3) ** n) / (K_ROS ** n + (ROS_rk4[i - 1] + k3) ** n)
    k4 = dt * (k_ROS - k_deg * SOD4 * (ROS_rk4[i - 1] + k3))

    ROS_rk4[i] = ROS_rk4[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    SOD_rk4[i - 1] = SOD1

# SOD transcription efficiency at the last time point
SOD_rk4[-1] = k_SOD * (ROS_rk4[-1] ** n) / (K_ROS ** n + ROS_rk4[-1] ** n)