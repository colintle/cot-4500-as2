import numpy as np

def neville(x, f_x, x_target):
    n = len(x)
    p = np.zeros((n, n))

    p[:, 0] = f_x

    for j in range(1, n):
        for i in range(n-j):
            p[i][j] = ((x_target - x[i+j]) * p[i][j-1] + (x[i] - x_target) * p[i+1][j-1]) / (x[i] - x[i+j])

    return p[0][n-1]

def divided_difference(xi, fi):
    n = len(xi)
    diff = np.zeros((n, n))

    for i in range(n):
        diff[i][0] = fi[i]

    for i in range(1, n):
        for j in range(1,i+1):
            diff[i][j] = (diff[i][j-1] - diff[i-1][j - 1]) / (xi[i] - xi[i-j])

    return diff

def return_last(xi, diffs):
    last= []
    for i in range(len(xi)):
        for j in range(i+1):
            if j == i:
                last.append(diffs[i][j])
    return [last]

def print_polynomial(xi, diffs, degree):
    terms = [f"{diffs[0][0]:.6f}"]
    for i in range(1, degree + 1):
        coeff = diffs[i][i]
        term = f"{coeff:+.6f}"
        if (term[0] == "+"): 
            term = term[1:]
        for j in range(i):
            term += f"*(x{-xi[j]:+.6f})"
        terms.append(term)
    polynomial = " + ".join(terms)
    return polynomial

def incremental_newton_polynomial(x, xi, diffs):
    polynomial = diffs[0][0]
    for i in range(1, len(xi)):
        term = diffs[0][i]
        for j in range(i):
            term *= (x - xi[j])
        polynomial += term
    return polynomial

