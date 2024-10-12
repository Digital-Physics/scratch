import numpy as np
import math

n = 1082
samples = []
confidence_interval_level = 0.90 # not used directly. assumed 1.645 z score for two tails of 5%
population_mean = 0.7
population_std = 0.01

def get_z_value(conf_level: float) -> float:
    """input should be between 0 and 1. 
    it's a percentile, and represents an area less than some value in a monotonically increasing cumulative distribution function.
    cdf(z) = conf_level
    returns a single-tailed z-score float between -inf and inf, but usually between -3 and 3"""

    percentile = conf_level if conf_level >= 0.5 else (1 - conf_level)

    cdf = 0.5 # half of a standard normal distribution is less than a z-score of 0; cdf(0)=0.5
    z_value = 0 
    delta = 0.0001 # we want to see familiar z-scores so 4 orders of precision is good for 1.645

    while cdf < percentile:
        # print(f"{cdf=}, {z_value=}")
        z_value += delta
        # almost calculus. add the area of a rectangle of width delta and height pdf(z)
        cdf += delta * ((1 / (math.sqrt(2 * math.pi))) * math.exp(-0.5 * (z_value ** 2)))

    return z_value if conf_level >= 0.5 else -z_value

for _ in range (n):
    sample = np.random.normal(population_mean, population_std)
    samples.append(sample)

sample_avg = sum(samples)/n
sample_var = sum([(samples[i] - sample_avg)**2 for i in range(n)])/(n-1) # estimate of the population variance
sample_std = np.sqrt(sample_var)

# we use the sample std in place of the population std. we divided by n-1, so it should be unbiased.
sem = sample_std/np.sqrt(n) # standard error of (estimating) the (population) mean (with a sampling of size n)

z_score = get_z_value((1 + confidence_interval_level)/2)  # for a 90% confidence interval, you want a cdf(z) = 0.95 and cdf(-z) = 0.05
print(f"{z_score=} {z_score=:.3f}")
print(f"{get_z_value(0.05)=}")

confidence_interval = (sample_avg - z_score * sem, sample_avg + z_score * sem)

print()
print(f"the sample average, which is an unbiased estimator of the population average: {sample_avg}")
print(f"Sample standard deviation, which has n-1 degrees of freedom, is an unbiased estimator of the standard deviation: {sample_std}")
print(f"Standard error of the (population) mean (i.e. the thing we're trying to estimate with samples): {sem}")
print(f"Confidence interval of the population mean at a {confidence_interval_level*100}% confidence level: {confidence_interval}")
print()
print("Is our n high enough? How wide is our confidence? What kind of percentage error are we looking at?")
print("upper confidence bound / average: ", confidence_interval[1] / sample_avg)
print("lower confidence bound / average: ", confidence_interval[0] / sample_avg)

print("look at t-statistic formula next and compare similarity")
print("t stat used for n < 30 or you don't have population standard deviation")
print("formula looks very similar, although (x - mu)/(sigma/sqrt(n)) is the denominator, not sigma*sqrt(n)")
print("division isn't associative. a/(b/c) != (a/b)/c")
print("multiplication is associative. but is a/b/c meant to be (a*(1/b))*(1/c) or a*1/(b*1/c) or what???? need to think!")