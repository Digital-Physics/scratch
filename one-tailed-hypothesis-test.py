import math
from scipy.stats import norm
import pandas as pd

# alternative hypothesis: the pumpkin has some negative pooping side effects on the cat (i.e. positive_poop_rate_before > pos_poop_rate_after)
# null hypothesis: the pumpkin has no effect or is beneficial for the cat's pooping (assume no effect for creating a p-value)
# note: we throw out the corn litter data. we also don't include no activity periods (df["Poop"] == 0)

df = pd.read_csv("Orville Poop Log.csv")
# print(df.columns)
# print(df["Litter Type"].describe)

# Define the counts of successes and total observations
success_without_pumpkin = df[(df["Pre-Pumpkin"] == 1)  & (df["Litter Type"]=="Clay") & (df["Poop"] == 1)].shape[0]
total_without_pumpkin = df[(df["Pre-Pumpkin"] == 1) & (df["Litter Type"]=="Clay") & ((df["Poop"] == 1) | (df["Poop"] == -1))].shape[0]
success_with_pumpkin = df[(df["Pre-Pumpkin"] == 0) & (df["Litter Type"]=="Clay") & (df["Poop"] == 1)].shape[0]
total_with_pumpkin = df[(df["Pre-Pumpkin"] == 0) & (df["Litter Type"]=="Clay") & ((df["Poop"] == 1) | (df["Poop"] == -1))].shape[0]

print(f"{success_without_pumpkin=}, {success_with_pumpkin=}, {total_without_pumpkin=}, {total_with_pumpkin=}")

# Calculate sample proportions
# 85% -> 71% 
p1 = success_without_pumpkin / total_without_pumpkin
p2 = success_with_pumpkin / total_with_pumpkin
print("before and after rates:", p1, p2)

# Calculate pooled proportion 
p = (success_without_pumpkin + success_with_pumpkin) / (total_without_pumpkin + total_with_pumpkin)

# Note: Standard error looks at All observations to get a rate p... 
# The standard error gives an idea of how much the sample mean (a metric) would vary if we repeatedly drew samples from the population.
# note: the more samples, the smaller we'd expect the mean to jump around e.g. (1/100000000 + 1/800000000 ~= 0)
SE = math.sqrt(p * (1 - p) * (1 / total_without_pumpkin + 1 / total_with_pumpkin))

# Calculate z-score
z_score = (p1 - p2) / SE

# Calculate p-value (one-tailed test)
p_value = (1 - norm.cdf(z_score))

# Display results
print(f"Z-score: {z_score}")
print(f"P-value: {p_value}")

if p_value < 0.05:
    print("reject the null hypothesis. there is only a 5% chance we'd see data this extreme if the that assumption were true")
else:
    print("we fail to reject the null hypothesis (that the post-pumpkin positive poop rate hasn't decreased) at the 0.05 level")