from math import sqrt

a = float(input())
b = float(input())
c = sqrt(a ** 2 + b ** 2)
val = "{:.3f}".format(c)

print(f"The length of the diagonal is {val}")
