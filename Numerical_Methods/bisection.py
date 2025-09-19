# import matplotlib.pyplot as plt
# import numpy as np

# def bisection_method(f, a, b, tolerate = 1e-6):
#     if f(a) * f(b) >= 0:
#         raise ValueError("f(a) & f(b) must have opposite signs.")
#     mid = (a + b) / 2.0

#     if abs (f(mid)) < tolerate:
#         return mid
#     elif f(a) * f(mid) < 0:
#         return bisection_method(f, a, mid, tolerate)
#     else:
#         return bisection_method(f, mid, b, tolerate)

# # Simple function
# def f(x):
#   return x**2 - 3

# root = bisection_method(f, 1, 3)

# # Let's plot the result
# x = np.arange(0, 3, 0.1)
# print(x)

# plt.plot(x, f(x))
# plt.axvline(root)

# plt.grid()
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

def bisection(f, a, b, tol=1e-6):
    if f(a)*f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    while True:
        c = (a + b)/2
        if abs(f(c)) < tol:
            return c
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
        
def f(x):
    return x**3 - 1

root = bisection(f, 0, 2)

x = np.arange(-3, 3, .0001)
print(x)
plt.plot(x,f(x))
plt.axvline(root)
plt.grid()
plt.show()