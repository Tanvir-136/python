import random
import math

def fun(x):
    return - ((x - 2) ** 2) + 4

# def hill_climb(fun, init, step=1, iteration=100):
#     x = init
#     for i in range(iteration):
#         if fun(x) < fun(x+step):
#             x += step
#         elif fun(x) < fun(x-step):
#             x -= step
#         else:
#             break
#         print(f"Step {i+1}: f({x}) - f({x+step}) - f({x-step})")
#     return x

# def hill_climb_random(fun, start=-10, stop=10, step=1, iteration=100):
#     x = random.randint(start, stop)
#     di = {}
#     for i in range(iteration):
#         if fun(x) < fun(x+step):
#             x += step
#         elif fun(x) < fun(x-step):
#             x -= step
#         else:
#             di[x] = fun(x)
#             x = random.randint(start, stop)
#         print(f"Step {i+1}: f({x}) - f({x+step}) - f({x-step})")
#     print(di)
#     return [i for i, j in di.items() if j == max(di.values())][0]

# # print(hill_climb(fun, random.randint(-10, 10), 1.5))
# print(hill_climb_random(fun, -10, 10, 1.5))




def simulated_annealing(fun, start=-10, stop=10, step=1, T=100, cooling=0.95):
    x = random.uniform(start, stop)
    best = x
    i = 0
    while T > 0.1:
        i += 1
        # Small random move (neighbor)
        x_new = x + random.uniform(-step, step)
        if x_new < start: x_new = start
        if x_new > stop: x_new = stop

        delta = fun(x_new) - fun(x)

        # Accept if better or with probability exp(delta/T)
        if delta > 0 or random.random() < math.exp(delta / T):
            x = x_new
            if fun(x) > fun(best):
                best = x

        print(f"[SA] Step {i}: T={T:.2f}, x={x:.2f}, f(x)={fun(x):.2f}")
        T *= cooling
    return best

print(simulated_annealing(fun))