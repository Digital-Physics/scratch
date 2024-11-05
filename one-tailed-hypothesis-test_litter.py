import math
from scipy.stats import norm
import pandas as pd

# null hypothesis: the corn litter has no effect or is beneficial for the cat's pooping (assume no effect for creating a p-value)
# alternative hypothesis: the corn litter has some negative pooping side effects on the cat (i.e. positive_poop_rate_with_clay > pos_poop_rate_with_corn)
# note: we also don't include no activity periods (df["Poop"] == 0)

df = pd.read_csv("Orville Poop Log.csv")

# Define the counts of successes and total observations
success_without_cornLitter = df[(df["Litter Type"]=="Clay") & (df["Poop"] == 1)].shape[0]
total_without_cornLitter = df[(df["Litter Type"]=="Clay") & ((df["Poop"] == 1) | (df["Poop"] == -1))].shape[0]
success_with_cornLitter = df[(df["Litter Type"]=="Corn") & (df["Poop"] == 1)].shape[0]
total_with_cornLitter = df[(df["Litter Type"]=="Corn") & ((df["Poop"] == 1) | (df["Poop"] == -1))].shape[0]

print(f"{success_without_cornLitter=}, {success_with_cornLitter=}, {total_without_cornLitter=}, {total_with_cornLitter=}")

# Calculate sample proportions
p1 = success_without_cornLitter / total_without_cornLitter
p2 = success_with_cornLitter / total_with_cornLitter
print("without corn litter (clay), with corn litter (pos poop rates):", p1, p2)

# Calculate pooled proportion 
p = (success_without_cornLitter + success_with_cornLitter) / (total_without_cornLitter + total_with_cornLitter)

# Note: Standard error looks at All observations to get a rate p... 
# The standard error gives an idea of how much the sample mean (a metric) would vary if we repeatedly drew samples from the population.
# note: the more samples, the smaller we'd expect the mean to jump around e.g. (1/100000000 + 1/800000000 ~= 0)
SE = math.sqrt(p * (1 - p) * (1 / total_without_cornLitter + 1 / total_with_cornLitter))

# Calculate z-score
z_score = (p1 - p2) / SE

# Calculate p-value (one-tailed test)
p_value = (1 - norm.cdf(z_score))

# Display results
print(f"Z-score: {z_score}")
print(f"P-value: {p_value}")

if p_value < 0.05:
    print("reject the null hypothesis (that the positive poop rate with clay litter hasn't increased). there is only a 5% chance we'd see data this extreme if the that assumption were true")
else:
    print("we fail to reject the null hypothesis (that the positive poop rate with clay layer hasn't increased) at the 0.05 level")