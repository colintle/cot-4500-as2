from src.main.assignment_2 import neville

#Question 1
x = [3.6, 3.8, 3.9]
f_x = [1.675, 1.436, 1.318]
target = 3.7

interpolated = neville(x, f_x, target)
print(interpolated)

