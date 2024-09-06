from variables import K1, K_1, K2, K3, K_3, K4, Km1, Km2, sod_total, sod_low, sod_high,ros

def Asymptote():
    value=0
    for ros in range(0,1000):
        sod_ros_low = ((sod_total - sod_high) * (Km2 + ros) - (sod_total - sod_low)) * ros / (ros + (Km2 + ros) ** 2)
        sod_ros_high = ((sod_total - sod_low) * (Km1 + ros) - (sod_total - sod_high)) * ros / (ros + (Km1 + ros) ** 2)
        V = K2 * sod_ros_high + K4 * sod_ros_low
        while value<=V:
            value+=10**(-13)
    return value

sod_ros_low=((sod_total-sod_high)*(Km2+ros)-(sod_total-sod_low))*ros/(ros+(Km2+ros)**2)
sod_ros_high=((sod_total-sod_low)*(Km1+ros)-(sod_total-sod_high))*ros/(ros+(Km1+ros)**2)
V=K2*sod_ros_high+K4*sod_ros_low

