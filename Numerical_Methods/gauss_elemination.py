import numpy as np
import matplotlib.pyplot as plt

def gauss_elimination(A, B):
    A = A.astype(float)
    B = B.astype(float)
    n = len(B)

    # Forward Elimination
    for i in range(n):
        # Partial Pivoting
        max_row = np.argmax(abs(A[i:, i])) + i
        if A[max_row, i] == 0:
            raise ValueError("Matrix is singular or has no unique solution.")
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
            B[[i, max_row]] = B[[max_row, i]]

        for j in range(i+1, n):
            ratio = A[j, i] / A[i, i]
            A[j, i:] -= ratio * A[i, i:]
            B[j] -= ratio * B[i]

    # Back Substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (B[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    return x

def plot_solution_2d(A, B, sol):
    x = np.linspace(-10, 10, 400)
    for i in range(A.shape[0]):
        a, b = A[i, 0], A[i, 1]
        if b != 0:
            y = (B[i] - a * x) / b
            plt.plot(x, y, label=f"Eq {i+1}")
    plt.plot(sol[0], sol[1], 'ro', label="Solution")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
    plt.axvline(0, color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.title("Solution of Linear Equations (2D)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Example system:
    # x + 2y = 8
    # 3x - y = 3
    A = np.array([[1, 2],
                  [3, -1]], dtype=float)
    B = np.array([8, 3], dtype=float)

    try:
        solution = gauss_elimination(A.copy(), B.copy())
        print("Solution:")
        for i, val in enumerate(solution):
            print(f"x{i+1} = {val:.6f}")
        
        if A.shape[1] == 2:
            plot_solution_2d(A, B, solution)

    except ValueError as e:
        print("Error:", e)