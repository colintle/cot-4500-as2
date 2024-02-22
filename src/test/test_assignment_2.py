from src.main.assignment_2 import neville, dividedDiff, returnLast, printPoly, newton, hermite, printTable, cubic

#Question 1
x = [3.6, 3.8, 3.9]
fX = [1.675, 1.436, 1.318]
target = 3.7

interpolated = neville(x, fX, target)
print(interpolated)
print()

#Question 2
xi = [7.2, 7.4, 7.5, 7.6]
fi = [23.5492, 25.3913, 26.8224, 27.4589]

diffs = dividedDiff(xi, fi)
polynomial_degree_1 = printPoly(xi, diffs, 1)
polynomial_degree_2 = printPoly(xi, diffs, 2)
polynomial_degree_3 = printPoly(xi, diffs, 3)

print(f"Polynomial of degree 1: P_1(x) = {polynomial_degree_1}")
print(f"Polynomial of degree 2: P_2(x) = {polynomial_degree_2}")
print(f"Polynomial of degree 3: P_3(x) = {polynomial_degree_3}")
print()

#Question 3
last = returnLast(xi, diffs)
x_value = 7.3

p1 = newton(x_value, xi[:2], [diff[:2] for diff in last])
p2 = newton(x_value, xi[:3], [diff[:3] for diff in last])
p3 = newton(x_value, xi[:4], [diff[:4] for diff in last])
print(p1)
print(p2)
print(p3)
print()

#Question 4
x = [3.6, 3.8, 3.9]
f = [1.675, 1.436, 1.318]
fPrime = [-1.195, -1.188, -1.182]
divided_diff = hermite(x, f, fPrime)
printTable(divided_diff)
print()

#Question 5
x = [2, 5, 8, 10]
y = [3, 5, 7, 9]

table = cubic(x, y)
print(table)
print(y)
print(x)


