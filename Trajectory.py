import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
rho = 1.225  # Air density (kg/m^3)
m = 0.43  # Mass of the ball (kg) - standard soccer ball
A = 0.04  # Cross-sectional area of the ball (m^2)
C_d = 0.47  # Drag coefficient (dimensionless)
alpha = (C_d * rho * A) / (2 * m)  # Drag parameter (1/s)

# Initial conditions
v0 = 30  # Initial velocity (m/s)
theta = 45 * np.pi / 180  # Launch angle in radians
u_x = v0 * np.cos(theta)  # Initial velocity in x-direction
u_y = v0 * np.sin(theta)  # Initial velocity in y-direction
x0 = 0  # Initial x position (m)
d = 0  # Initial y position (m)

# Time settings
t_max = 5  # Maximum simulation time (s)
t_steps = 1000  # Number of time steps
t = np.linspace(0, t_max, t_steps)  # Time array

# Velocity formulas
v_x = u_x * np.exp(-alpha * t)
v_y = (-g / alpha) + (u_y + g / alpha) * np.exp(-alpha * t)

# Position formulas
x = x0 + (u_x / alpha) * (1 - np.exp(-alpha * t))
y = (-g * t / alpha) - ((u_y + g / alpha) / alpha) * (1 - np.exp(-alpha * t)) + d

# Filter out negative y-values (ball hitting the ground)
valid_indices = y >= 0
x = x[valid_indices]
y = y[valid_indices]

# Plot the trajectory
plt.figure(figsize=(10, 5))
plt.plot(x, y, label="Trajectory with Air Resistance")
plt.title("Ball Trajectory with Air Resistance")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Distance (m)")
plt.legend()
plt.grid()
plt.show()
