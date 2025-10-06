# Braking Distance of a Car

# When a car brakes, the stopping distance s depends on its speed v and friction μ
#                   s=v^2/2μg
# Let’s say:
#   g=9.81 m/s2
#   μ=0.7
# We want the speed v at which the stopping distance is 40 meters.
#               f(v) = v^2/2μg - 40


import numpy as np
import matplotlib.pyplot as plt

# Constants
mu = 0.7       # friction coefficient
g = 9.81       # gravity (m/s^2)
s_target = 40  # stopping distance (m)

# Define the function
def f(v):
    return (v**2) / (2 * mu * g) - s_target

# Initial guesses (in m/s)
v0 = 20
v1 = 25

tol = 1e-6
max_iter = 50

# Secant Method
history = [v0, v1]
for i in range(max_iter):
    f0, f1 = f(v0), f(v1)
    v2 = v1 - f1 * (v1 - v0) / (f1 - f0)
    history.append(v2)
    if abs(v2 - v1) < tol:
        break
    v0, v1 = v1, v2

print(f"Car speed = {v2:.4f} m/s (after {i+1} iterations)")

# Plot
v_vals = np.linspace(10, 30, 200)
plt.plot(v_vals, f(v_vals), label="f(v) = v²/(2μg) - 40")
plt.axhline(0, color='gray', linestyle='--')
plt.scatter([v2], [0], color='red', label=f"Root (v ≈ {v2:.2f} m/s)")
plt.xlabel("Speed (m/s)")
plt.ylabel("f(v)")
plt.title("Secant Method — Car Braking Distance Example")
plt.legend()
plt.grid(True)
plt.show()
