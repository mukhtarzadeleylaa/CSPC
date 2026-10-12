import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("PW2/Lab B/kinetics.csv", delimiter=",", skiprows=1)

t = data[:, 0]
C = data[:, 1]
C0 = C[0]

def total_error(k):
    predicted = C0 * np.exp(-k * t)
    return np.sum((C - predicted)**2)

from scipy.optimize import minimize_scalar

result = minimize_scalar(total_error, bounds=(0, 10), method="bounded")

k = result.x

print("Reaction rate k =", k)  

plt.scatter(t, C, color="blue", label="Measured data")
plt.plot(t, C0 * np.exp(-k * t), color="red", label="Fitted curve")

plt.xlabel("Time")
plt.ylabel("Concentration")
plt.legend()

plt.savefig("PW2/Lab B/kinetics.png")
plt.show()