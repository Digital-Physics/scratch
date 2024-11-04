import math
from scipy.stats import norm
import pandas as pd

df = pd.read_csv("Orville Poop Log.csv")

# Define the counts of successes and total observations
# 28 out of 40 successful cat poops before 
# 18 out of 20 successful cat poops after the introduction of pumpkin in diet 
# Successes and total observations in both groups
# The numbers commented out should give a more reasonable p-value of around 0.08... because it's plausible with these numbers there was a change
# success_without_pumpkin = 28
# total_without_pumpkin = 40
# success_with_pumpkin = 18
# total_with_pumpkin = 20
success_without_pumpkin = df[(df["Pre-Pumpkin"] == 1) & (df["Poop"] == 1)].shape[0]
total_without_pumpkin = df[(df["Pre-Pumpkin"] == 1) & ((df["Poop"] == 1) | (df["Poop"] == -1))].shape[0]
success_with_pumpkin = df[(df["Pre-Pumpkin"] == 0) & (df["Poop"] == 1)].shape[0]
total_with_pumpkin = df[(df["Pre-Pumpkin"] == 0) & ((df["Poop"] == 1) | (df["Poop"] == -1))].shape[0]

print(f"{success_without_pumpkin=}, {success_with_pumpkin=}, {total_without_pumpkin=}, {total_with_pumpkin=}")

# Calculate sample proportions
# 70% -> 90% (using 40 + 20 samples)
# 71.9% -> 71.4% (using actual data)
p1 = success_without_pumpkin / total_without_pumpkin
p2 = success_with_pumpkin / total_with_pumpkin
print("before and after rates:", p1, p2)

# Calculate pooled proportion (76%)
p = (success_without_pumpkin + success_with_pumpkin) / (total_without_pumpkin + total_with_pumpkin)

# Note: Standard error looks at All observations to get a rate p... 
# The standard error gives an idea of how much the sample mean (a metric) would vary if we repeatedly drew samples from the population.
# note: the more samples, the smaller the error e.g. (1/100000000 + 1/800000000 ~= 0)
SE = math.sqrt(p * (1 - p) * (1 / total_without_pumpkin + 1 / total_with_pumpkin))

# Calculate z-score
z_score = (p1 - p2) / SE

# Calculate p-value (two-tailed test)
p_value = 2 * (1 - norm.cdf(abs(z_score)))

# Display results
print(f"Z-score: {z_score}")
print(f"P-value: {p_value}")

if p_value < 0.05:
    print("reject the null hypothesis. there is only a 5% chance we'd see data this extreme if the that assumption were true")
else:
    print("we fail to reject the null hypothesis (that there is no difference) at the 0.05 level")