k_ROS = 1.0  # ROS generation rate constant
k_deg = 0.1  # ROS degradation rate constant
k_SOD = 2.0  # The maximum value of SOD transcription efficiency
K_ROS = 1.0  # Half inhibitory concentration of ROS
n = 2.0  # Synergy coefficient
ROS_0 = 0.1  # Initial ROS concentration

T = 50  # time
dt = 0.01  # Time step
steps = int(T / dt)  # steps