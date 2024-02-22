import numpy as np

def neville(x, f_x, x_target):
    n = len(x)
    p = np.zeros((n, n))

    p[:, 0] = f_x

    for j in range(1, n):
        for i in range(n-j):
            p[i][j] = ((x_target - x[i+j]) * p[i][j-1] + (x[i] - x_target) * p[i+1][j-1]) / (x[i] - x[i+j])

    return p[0][n-1]
