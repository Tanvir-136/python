# Gauss-Jordan Method

N = 3
arr = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
    ]

def gauss_jordan(arr, N):
    for i in range(N):
        for j in range(N):
            if i != j:
                p = arr[j][i] / arr[i][i]
                for k in range(N+1):
                    arr[j][k] -= arr[i][k] * p

    for i in range(N):
        print(arr[i][3] / arr[i][i])

gauss_jordan(arr, N)

# ans: [2.0 , 3.0, -1.0]