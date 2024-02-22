from src.main.assignment_2 import neville, divided_difference, return_last, print_polynomial, incremental_newton_polynomial
import numpy as np

#Question 1
x = [3.6, 3.8, 3.9]
f_x = [1.675, 1.436, 1.318]
target = 3.7

interpolated = neville(x, f_x, target)
print(interpolated)
print()

#Question 2
xi = [7.2, 7.4, 7.5, 7.6]
fi = [23.5492, 25.3913, 26.8224, 27.4589]

diffs = divided_difference(xi, fi)
polynomial_degree_1 = print_polynomial(xi, diffs, 1)
polynomial_degree_2 = print_polynomial(xi, diffs, 2)
polynomial_degree_3 = print_polynomial(xi, diffs, 3)

print(f"Polynomial of degree 1: P_1(x) = {polynomial_degree_1}")
print(f"Polynomial of degree 2: P_2(x) = {polynomial_degree_2}")
print(f"Polynomial of degree 3: P_3(x) = {polynomial_degree_3}")
print()

#Question 3
last = return_last(xi, diffs)
x_value = 7.3

p1 = incremental_newton_polynomial(x_value, xi[:2], [diff[:2] for diff in last])
p2 = incremental_newton_polynomial(x_value, xi[:3], [diff[:3] for diff in last])
p3 = incremental_newton_polynomial(x_value, xi[:4], [diff[:4] for diff in last])
print(p1)
print(p2)
print(p3)


