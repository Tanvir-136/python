import numpy as np
import matplotlib.pyplot as plt

# ODE: dv/dt = -k/m * v
def f(t, v, k=50, m=1000):
    return -(k/m) * v

# Parameters
t0, v0 = 0, 30   # initial time and velocity
h = 1            # step size
n = 20           # number of steps
k, m = 50, 1000

# Arrays to store results
t = [t0]
v = [v0]

# Step 1: Generate first 3 points using RK4
def rk4_step(t, v, h):
    k1 = f(t, v, k, m)
    k2 = f(t + h/2, v + h*k1/2, k, m)
    k3 = f(t + h/2, v + h*k2/2, k, m)
    k4 = f(t + h, v + h*k3, k, m)
    return v + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

for i in range(3):
    v.append(rk4_step(t[i], v[i], h))
    t.append(t[i] + h)

# Step 2: Milne’s Predictor-Corrector 
for i in range(3, n):
    t_next = t[i] + h
    
    # Milne’s Predictor formula
    v_pred = v[i-3] + (4*h/3) * (2*f(t[i-2], v[i-2], k, m) 
                                 - f(t[i-1], v[i-1], k, m) 
                                 + 2*f(t[i], v[i], k, m))
    
    # Milne’s Corrector formula
    v_corr = v[i-1] + (h/3) * (f(t[i-1], v[i-1], k, m) 
                               + 4*f(t[i], v[i], k, m) 
                               + f(t_next, v_pred, k, m))
    
    t.append(t_next)
    v.append(v_corr)

# Convert to numpy arrays
t = np.array(t)
v = np.array(v)

# Exact solution for comparison
v_exact = v0 * np.exp(-(k/m)*t)

# Plotting 
plt.figure(figsize=(8,5))
plt.plot(t, v, 'o-', label="Milne’s Method (numerical)", color="blue")
plt.plot(t, v_exact, 'r--', label="Exact solution", linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Car Velocity Under Air Resistance (Milne’s Method)")
plt.legend()
plt.grid(True)
plt.show()