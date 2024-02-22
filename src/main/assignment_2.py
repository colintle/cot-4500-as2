import numpy as np
from scipy.interpolate import CubicSpline

def neville(x, fX, target):
    n = len(x)
    table = np.zeros((n, n))

    table[:, 0] = fX

    for j in range(1, n):
        for i in range(n-j):
            table[i][j] = ((target - x[i+j]) * table[i][j-1] + (x[i] - target) * table[i+1][j-1]) / (x[i] - x[i+j])

    return table[0][n-1]

def dividedDiff(xi, fi):
    n = len(xi)
    diff = np.zeros((n, n))

    for i in range(n):
        diff[i][0] = fi[i]

    for i in range(1, n):
        for j in range(1,i+1):
            diff[i][j] = (diff[i][j-1] - diff[i-1][j - 1]) / (xi[i] - xi[i-j])

    return diff

def returnLast(xi, diffs):
    last= []
    for i in range(len(xi)):
        for j in range(i+1):
            if j == i:
                last.append(diffs[i][j])
    return [last]

def printPoly(xi, diffs, degree):
    terms = [f"{diffs[0][0]:.6f}"]
    for i in range(1, degree + 1):
        coeff = diffs[i][i]
        term = f"{coeff:+.6f}"
        if (term[0] == "+"): 
            term = term[1:]

        for j in range(i):
            term += f"*(x{-xi[j]:+.6f})"

        terms.append(term)

    poly = " + ".join(terms)
    return poly

def newton(x, xi, diffs):
    poly = diffs[0][0]
    for i in range(1, len(xi)):
        term = diffs[0][i]
        for j in range(i):
            term *= (x - xi[j])
        poly += term
    return poly

def hermite(x, f, fPrime):
    n = len(x)
    diff = np.zeros((2*n, 2*n))

    for i in range(n):
        diff[2*i][0] = f[i]
        diff[2*i+1][0] = f[i]
        diff[2*i+1][1] = fPrime[i]
        if i != 0:
            diff[2*i][1] = (diff[2*i][0] - diff[2*i-1][0]) / (x[i] - x[i-1])

    for i in range(2, 2*n):
        for j in range(2, i+1):
            diff[i][j] = (diff[i][j-1] - diff[i-1][j-1]) / (x[i//2] - x[(i-j)//2])

    return diff

def printTable(table):
    for row in table:
        print("  ".join(f"{value: .8f}" if isinstance(value, float) else str(value) for value in row))

def cubic(x, y):
    cs = CubicSpline(x, y, bc_type='natural')
    A = np.array(cs.c).T
    return A


