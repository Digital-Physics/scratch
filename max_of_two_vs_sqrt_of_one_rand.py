# watch 3blue1brown video here:
# https://www.youtube.com/watch?v=Pny70rNPJLk
import random
import math
import matplotlib.pyplot as plt

# Generate 100000 random numbers and compute their square roots and cube roots
random_numbers = [random.random() for _ in range(100000)]
sqrts = [math.sqrt(num) for num in random_numbers]
cube_roots = [math.pow(num, 1/3) for num in random_numbers]

# Generate 100000 max values from two and three random numbers
maxs_two = [max(random.random(), random.random()) for _ in range(100000)]
maxs_three = [max(random.random(), random.random(), random.random()) for _ in range(100000)]

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))  # 2 rows, 2 columns

# Plot the distribution of sqrt()
axes[0, 0].hist(sqrts, bins=100, edgecolor='black')
axes[0, 0].set_title("Distribution of sqrt() on a uniform RV from 0 to 1")
axes[0, 0].set_xlabel("Value")
axes[0, 0].set_ylabel("Frequency")

# Plot the distribution of cube root
axes[0, 1].hist(cube_roots, bins=100, edgecolor='black')
axes[0, 1].set_title("Distribution of cube root on a uniform RV from 0 to 1")
axes[0, 1].set_xlabel("Value")
axes[0, 1].set_ylabel("Frequency")

# Plot the distribution of max() on two RVs
axes[1, 0].hist(maxs_two, bins=100, edgecolor='black')
axes[1, 0].set_title("Distribution of max() on two uniform RVs")
axes[1, 0].set_xlabel("Value")
axes[1, 0].set_ylabel("Frequency")

# Plot the distribution of max() on three RVs
axes[1, 1].hist(maxs_three, bins=100, edgecolor='black')
axes[1, 1].set_title("Distribution of max() on three uniform RVs")
axes[1, 1].set_xlabel("Value")
axes[1, 1].set_ylabel("Frequency")

# Adjust layout and show the plot
plt.tight_layout()
plt.show()

