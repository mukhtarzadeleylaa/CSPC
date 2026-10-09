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