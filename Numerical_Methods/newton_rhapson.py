# Suppose you drop a small metal ball into water and want to find the depth h (in meters) 
# where the water pressure equals 300,000 Pascals (Pa).

# The pressure under water is given by:

#                           P=P0+ρgh

# So we need to solve:

#                       f(h)=P0+ρgh−300000=0

import numpy as np
import matplotlib.pyplot as plt

# Constants
P0 = 101325      # Atmospheric pressure (Pa)
rho = 1000       # Density of water (kg/m^3)
g = 9.81         # Gravitational acceleration (m/s^2)
P_target = 300000  # Desired pressure (Pa)

# Define function and derivative
def f(h):
    return P0 + rho * g * h - P_target

def f_prime(h):
    return rho * g  # derivative of f(h) with respect to h

# Newton-Raphson iteration
h = 5.0  # initial guess (meters)
tolerance = 1e-6
max_iter = 20
history = [h]

for i in range(max_iter):
    h_new = h - f(h) / f_prime(h)
    history.append(h_new)
    if abs(h_new - h) < tolerance:
        break
    h = h_new

print(f"Depth h = {h_new:.4f} meters after {i+1} iterations")

# Plot convergence
plt.plot(history, 'o-', label='h values')
plt.xlabel('Iteration')
plt.ylabel('Depth (m)')
plt.title('Newton-Raphson Convergence for Water Pressure')
plt.grid(True)
plt.legend()
plt.show()
