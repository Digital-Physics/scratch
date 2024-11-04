from scipy.interpolate import BSpline
import numpy as np
import matplotlib.pyplot as plt

# Define knots and degree of spline
knots = [0, 1, 2, 3, 4, 5, 6, 10]
degree = 3  # cubic B-spline

# Define B-spline coefficients (can be fitted to data)
coefficients = [1, 2, 0, -1, 1, 0, 2]

# Create B-spline object
spline = BSpline(knots, coefficients, degree)

# Plot the B-spline
x = np.linspace(0, 6, 100)
y = spline(x)
plt.plot(x, y)
plt.title("Cubic B-Spline Example")
plt.show()