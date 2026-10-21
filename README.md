# CSPC - Computer Science for Physics and Chemistry
My coursework for CSPC.

## Setup

conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc

---

## PW1 - Lab A: Reproducible Foundations

**what I did:**
- I made a conda environment.
- I added the decay files.
- I used Git and GitHub.
- I made tests with pytest.

**speed comparison:**
- loop: 2.657672 s
- numpy: 0.000288 s
- speed-up: 9236.18x faster

**tests:** all 3 tests passed

**conclusion:**
- NumPy was much faster.
- I learned how to use conda, Git, GitHub and pytest.
- At first some things were confusing, but now I understand the basic steps better<3

## PW2 - Lab A: Motion from Tracking Data
**Results:**
- Mean acceleration: -8.58 m/s²
- Expected acceleration: -9.81 m/s²

**Noise observation:**
The measured acceleration is close to -9.81 m/s², but it is noisy. Small errors in position measurements become larger when calculating derivatives, especially acceleration.

## PW2 - Lab b: Optimization
**Objective:**
Compare three optimization methods: Gradient Descent, Newton's Method, and SLSQP.

**Results for f(x):**
- Gradient Descent: x ≈ 3.0
- Newton's Method: x = 3.0
- SLSQP: x = 3.0

All three methods found the minimum at x = 3.

**Results for g(x):**
- Gradient Descent (x0=0): x ≈ -1.30084
- Newton's Method (x0=0): x ≈ 0.16994
- SLSQP (x0=0): x ≈ -1.30086
- SLSQP (x0=2): x ≈ -1.30064
- SLSQP (x0=1): x ≈ 1.13090

**Analysis:**

Gradient Descent and SLSQP found a minimum near x = -1.30.

SLSQP also found another local minimum near x = 1.13 when starting from x0 = 1.

Newton's Method converged to x = 0.17, which is a local maximum, not a minimum.

This shows that optimization methods can give different results depending on the starting point and the method used.

**Optimization Graph:**

![Optimization Graph](PW2/Lab%20B/optimization.png)

### Part 3 - Chemistry 1: Reaction Rate

**Fitted rate constant:** k = 0.26176

The fitted curve closely matches the measured data.

![Kinetics Graph](PW2/Lab%20B/kinetics.png)

**Chemical Equilibrium Results:**
- Newton: x ≈ 0.66385
- SLSQP: x ≈ 0.66385
- H2 = 0.33615 mol
- I2 = 0.33615 mol
- HI = 1.32770 mol

Both methods agree and give the same equilibrium point.

![Chemical Equilibrium](PW2/Lab%20B/equilibrium.png)



## PW3 - Statistical Analysis

### Normality Tests
We used the Shapiro-Wilk test to check if our four variables are normally distributed.

The results were:

* Age: p = 0.00607
* Cholesterol: p = 5.91e-09
* Blood Pressure: p = 1.80e-06
* Maximum Heart Rate: p = 6.996e-05

All the p-values are smaller than 0.05, so none of the four variables passed the normality test.

From the histograms, some distributions look close to normal, but they are not perfectly symmetric. We can also see some extreme values, especially for cholesterol.



Heart Rate Comparison

We wanted to check if healthy people and people with heart disease have different maximum heart rates.

We compared 164 healthy patients and 139 patients with heart disease. The average maximum heart rate was 158.38 bpm for healthy patients and 139.26 bpm for patients with heart disease.

We used the Mann-Whitney U test because the data was not normally distributed. The p-value was 1.86e-13, which is smaller than 0.05. This means there is a significant difference between the two groups.

We also made a bar chart with error bars. The standard error was 1.50 for healthy patients and 1.92 for patients with heart disease. The graph supports our results.

Age and Maximum Heart Rate

We wanted to see if age and maximum heart rate are related.

The correlation was -0.394, which shows a moderate negative relationship.

We made a scatter plot and saw that maximum heart rate generally decreases as people get older. However, this is not always the case for everyone.

Chemicals and Cancer

We wanted to find out which chemical is more strongly related to malignancy.

First, we calculated the correlations:

* Benzene: 0.385
* Cadmium: 0.880

At first, cadmium seemed to have a stronger relationship with malignancy because its correlation was much higher.

Checking the Effect of Pollution

We wanted to check if pollution was affecting our results.

We selected patients with a pollution index between 40 and 60. There were 199 patients in this group.

After filtering, the correlations were:

* Benzene: 0.702
* Cadmium: 0.316

We noticed that the correlation for benzene increased, while the correlation for cadmium decreased.

This suggests that pollution was affecting the original results. Benzene seems more likely to be directly related to malignancy, while cadmium may have looked strongly related because of pollution.

However, correlation does not prove causation, so we cannot be completely sure from this analysis alone.

Conclusion

In this practical work, we used statistical tests and graphs to study different relationships.

We found that healthy patients had a higher maximum heart rate on average and that maximum heart rate generally decreases with age.

We also learned that correlation does not always mean causation. In the chemical dataset, our results changed after we considered pollution, showing why it is important to check other factors before making conclusions.