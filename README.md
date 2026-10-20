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

These results will help us choose the right statistical tests for the next part.